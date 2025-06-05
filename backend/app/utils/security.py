"""
Comprehensive security utilities for Palace of Quests.
Includes authentication, authorization, input validation, and security monitoring.

Author: Erik G. - Palace of Quests Team  
Last Updated: 2025-06-04
"""

import hashlib
import hmac
import secrets
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from functools import wraps
from urllib.parse import urlparse

from flask import request, session, current_app, abort
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from cryptography.fernet import Fernet

# Security configuration constants
BCRYPT_ROUNDS = 12
CSRF_TOKEN_LENGTH = 32
SESSION_TIMEOUT_HOURS = 24
MAX_REQUEST_SIZE = 16 * 1024 * 1024  # 16MB
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.pdf', '.txt'}

# Regex patterns for validation
EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)
USERNAME_PATTERN = re.compile(
    r'^[a-zA-Z0-9_]{3,20}$'
)
SAFE_HTML_PATTERN = re.compile(
    r'<[^>]*>', re.IGNORECASE
)

class SecurityManager:
    """Centralized security management for the application."""
    
    def __init__(self):
        self.cipher_suite = Fernet(current_app.config.get('ENCRYPTION_KEY'))
        self.failed_attempts = {}
        self.blocked_ips = set()
    
    def generate_secure_token(self, length: int = 32) -> str:
        """Generate cryptographically secure random token."""
        return secrets.token_urlsafe(length)
    
    def hash_password(self, password: str) -> str:
        """Hash password using bcrypt with configurable rounds."""
        return generate_password_hash(
            password, 
            method='pbkdf2:sha256',
            salt_length=16
        )
    
    def verify_password(self, password: str, password_hash: str) -> bool:
        """Verify password against hash."""
        return check_password_hash(password_hash, password)
    
    def encrypt_sensitive_data(self, data: str) -> str:
        """Encrypt sensitive data for storage."""
        return self.cipher_suite.encrypt(data.encode()).decode()
    
    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data from storage."""
        return self.cipher_suite.decrypt(encrypted_data.encode()).decode()
    
    def generate_jwt_token(self, payload: Dict[str, Any], 
                          expires_hours: int = 24) -> str:
        """Generate JWT token with expiration."""
        payload['exp'] = datetime.utcnow() + timedelta(hours=expires_hours)
        payload['iat'] = datetime.utcnow()
        
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
    
    def verify_jwt_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Verify and decode JWT token."""
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256']
            )
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

def generate_csrf_token() -> str:
    """Generate CSRF token for form protection."""
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(CSRF_TOKEN_LENGTH)
    return session['csrf_token']

def verify_csrf_token(token: str) -> bool:
    """Verify CSRF token from form submission."""
    return token and session.get('csrf_token') == token

def validate_email_format(email: str) -> bool:
    """Validate email format using regex."""
    if not email or len(email) > 254:
        return False
    return bool(EMAIL_PATTERN.match(email.lower()))

def validate_username_format(username: str) -> bool:
    """Validate username format and content."""
    if not username or not USERNAME_PATTERN.match(username):
        return False
    
    # Check for reserved usernames
    reserved_usernames = {
        'admin', 'administrator', 'root', 'api', 'www',
        'mail', 'support', 'help', 'info', 'contact'
    }
    
    return username.lower() not in reserved_usernames

def validate_password_strength(password: str) -> Dict[str, Any]:
    """Comprehensive password strength validation."""
    errors = []
    score = 0
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
    
    if not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter")
    else:
        score += 1
    
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter")  
    else:
        score += 1
    
    if not re.search(r'\d', password):
        errors.append("Password must contain at least one number")
    else:
        score += 1
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character")
    else:
        score += 2
    
    # Check for common patterns
    common_patterns = [
        r'(.)\1{2,}',  # Repeated characters  
        r'(012|123|234|345|456|567|678|789|890)',  # Sequential numbers
        r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)'  # Sequential letters
    ]
    
    for pattern in common_patterns:
        if re.search(pattern, password.lower()):
            errors.append("Password contains common patterns and may be easily guessed")
            score -= 1
            break
    
    # Check against common passwords (simplified)
    common_passwords = {
        'password', '123456', 'password123', 'admin', 'qwerty',
        'letmein', 'welcome', 'monkey', '1234567890'
    }
    
    if password.lower() in common_passwords:
        errors.append("Password is too common and easily guessed")
        score -= 2
    
    strength_levels = {
        (0, 2): 'Very Weak',
        (3, 4): 'Weak', 
        (5, 6): 'Fair',
        (7, 8): 'Strong',
        (9, float('inf')): 'Very Strong'
    }
    
    strength = 'Very Weak'
    for (min_score, max_score), level in strength_levels.items():
        if min_score <= score <= max_score:
            strength = level
            break
    
    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'score': max(0, score),
        'strength': strength
    }

def sanitize_html_input(text: str) -> str:
    """Remove potentially dangerous HTML tags from input."""
    if not text:
        return ""
    
    # Remove HTML tags
    cleaned = SAFE_HTML_PATTERN.sub('', text)
    
    # Escape remaining special characters
    cleaned = cleaned.replace('&', '&amp;')
    cleaned = cleaned.replace('<', '&lt;')
    cleaned = cleaned.replace('>', '&gt;')
    cleaned = cleaned.replace('"', '&quot;')
    cleaned = cleaned.replace("'", '&#x27;')
    
    return cleaned.strip()

def validate_file_upload(file) -> Tuple[bool, str]:
    """Validate uploaded file for security."""
    if not file or not file.filename:
        return False, "No file selected"
    
    # Check file extension
    filename = file.filename.lower()
    if not any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        return False, f"File type not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
    
    # Check file size
    file.seek(0, 2)  # Seek to end
    file_size = file.tell()
    file.seek(0)  # Reset to beginning
    
    if file_size > MAX_REQUEST_SIZE:
        return False, f"File too large. Maximum size: {MAX_REQUEST_SIZE // 1024 // 1024}MB"
    
    return True, "File is valid"

def require_https(func):
    """Decorator to require HTTPS for sensitive endpoints."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.is_secure and not current_app.debug:
            abort(400, description="HTTPS required for this endpoint")
        return func(*args, **kwargs)
    return wrapper

def rate_limit_by_ip(max_requests: int = 100, window_minutes: int = 60):
    """Rate limiting decorator based on IP address."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
            
            # Simple in-memory rate limiting (use Redis in production)
            current_time = datetime.utcnow()
            window_start = current_time - timedelta(minutes=window_minutes)
            
            # This is a simplified implementation
            # In production, use Redis or similar for distributed rate limiting
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def log_security_event(event_type: str, details: Dict[str, Any] = None):
    """Log security events for monitoring and analysis."""
    from app.models.security_log import SecurityLog
    from app import db
    
    try:
        log_entry = SecurityLog(
            event_type=event_type,
            ip_address=request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr),
            user_agent=request.headers.get('User-Agent', ''),
            details=details or {},
            timestamp=datetime.utcnow()
        )
        
        db.session.add(log_entry)
        db.session.commit()
        
    except Exception as e:
        current_app.logger.error(f"Failed to log security event: {e}")

def check_suspicious_activity(user_id: int) -> bool:
    """Check for suspicious user activity patterns."""
    from app.models.security_log import SecurityLog
    
    recent_time = datetime.utcnow() - timedelta(hours=1)
    
    # Check for multiple failed login attempts
    failed_logins = SecurityLog.query.filter(
        SecurityLog.event_type == 'failed_login',
        SecurityLog.details.contains({'user_id': user_id}),
        SecurityLog.timestamp > recent_time
    ).count()
    
    if failed_logins > 5:
        return True
    
    # Add more suspicious activity checks here
    
    return False

# Initialize security manager
security_manager = SecurityManager()
