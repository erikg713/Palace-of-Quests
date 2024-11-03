# PiQuest - Web3 Game on Pi Network

## Overview
PiQuest is a Web3 quest-based RPG game where players explore a digital universe, earn Pi tokens, and complete challenges.

### Key Features
- Quest-based RPG mechanics
- NFT marketplace for trading in-game items
- Integration with Pi Network for token transactions

### Technologies Used
- Backend: Flask, PostgreSQL
- Frontend: React
- Authentication: JWT

## Setup Instructions

### Backend
1. Navigate to the `backend` folder.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python app.py`

### Frontend
1. Navigate to the `frontend` folder.
2. Install dependencies: `npm install`
3. Start the app: `npm start`

PiQuest Project Structure

Project Overview

The PiQuest structure is organized for a full-stack Web3 metaverse application with:

Frontend: React (with Three.js for 3D elements) optimized for mobile and Pi Network compatibility.

Backend: Flask API with JWT authentication, secure password hashing, and robust error handling.

Database: PostgreSQL with secure access control, structured for optimal performance with relational tables.


Unified Project Structure

piquest/
├── frontend/                  # Frontend - React application
│   ├── public/
│   │   ├── index.html         # Main HTML file for React
│   │   ├── manifest.json      # Manifest for PWA setup
│   │   └── icons/             # Icons for PWA and mobile devices
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   │   ├── MobileNav.js   # Bottom nav component for mobile
│   │   │   └── ThreeDScene.js # 3D scene component (Three.js)
│   │   ├── pages/             # Main pages for routing
│   │   │   ├── Home.js        # Home screen
│   │   │   ├── Marketplace.js # Marketplace page
│   │   │   └── Profile.js     # User profile page
│   │   ├── styles/            # CSS and styling files
│   │   │   ├── global.css     # Global styles with responsive layout
│   │   │   └── MobileNav.css  # Styles for MobileNav component
│   │   ├── api/               # API calls with error handling
│   │   │   └── auth.js        # Authentication API with error handling
│   │   ├── App.js             # Root React component for routing
│   │   └── index.js           # Entry point for rendering App
│   ├── .env                   # Frontend environment variables
│   └── README.md              # Frontend README
│
├── backend/                   # Backend - Flask REST API
│   ├── app/
│   │   ├── __init__.py        # App initialization
│   │   ├── models.py          # Database models (User, Inventory, Quests)
│   │   ├── routes/            # API route definitions
│   │   │   ├── auth.py        # Authentication routes
│   │   │   ├── marketplace.py # Marketplace routes
│   │   │   └── quests.py      # Game quests routes
│   │   ├── utils/             # Utility functions
│   │   │   ├── security.py    # Password hashing, JWT creation
│   │   └── error_handler.py   # Centralized error handling
│   ├── migrations/            # Database migrations
│   ├── config.py              # Secure configuration management
│   ├── .env                   # Backend environment variables
│   ├── requirements.txt       # Backend dependencies
│   ├── run.py                 # Entry point for Flask app
│   └── README.md              # Backend README
│
├── database/                  # Database - PostgreSQL scripts and setup
│   ├── schema.sql             # Initial schema setup for tables
│   ├── seed.sql               # Seed data for initial testing
│   ├── roles.sql              # Role-based access control setup
│   └── README.md              # Database README
│
├── .gitignore                 # Ignore node_modules, .env, etc.
├── docker-compose.yml         # Docker Compose for running services
├── README.md                  # Master README with setup instructions
└── LICENSE                    # Project license


---

Detailed Explanation of Each Directory and Key Files

1. Frontend Directory (frontend/)

The frontend directory contains a mobile-optimized React app integrated with Pi Network for a Web3 experience.

public/manifest.json: Configures the Progressive Web App (PWA) for Pi Network compatibility, with required icons.

src/components/: Houses reusable UI components, such as MobileNav.js for responsive mobile navigation and ThreeDScene.js for 3D interactions with Three.js.

src/pages/: Contains key pages (e.g., Marketplace.js) for the main features of the app, each with error handling and secure data fetching.

src/api/auth.js: API utility for handling authentication calls, with centralized error handling and secure token management.

.env: Stores frontend environment variables, keeping secrets out of source control.


2. Backend Directory (backend/)

The backend directory hosts a secure Flask REST API, handling user authentication, game mechanics, and marketplace interactions.

app/__init__.py: Initializes the Flask app, loads configurations, and sets up database connections.

app/models.py: Defines relational database models (e.g., User, Inventory, and Quests) and relationships, with indexes for performance.

app/routes/:

auth.py: Handles registration, login, and secure JWT-based authentication.

marketplace.py: Manages marketplace item listing, buying, and selling.

quests.py: Routes for quest creation, tracking, and completion rewards.


app/utils/security.py: Contains security functions for hashing passwords, creating JWT tokens, and managing token expiration.

app/error_handler.py: Provides centralized error handling for consistency, with error responses (e.g., 404, 500).

config.py: Central configuration file, loaded with environment variables for security, including SECRET_KEY, JWT_SECRET_KEY, and DATABASE_URL.

.env: Contains backend secrets like JWT keys and database URLs, secured and hidden from source control.


3. Database Directory (database/)

The database directory includes scripts for setting up PostgreSQL with secure access control and relational structures.

schema.sql: Defines the database schema for Users, Inventory, Quests, and Transactions tables, optimized with indexes on frequently accessed columns.

seed.sql: Optional seed data for testing and initial setup.

roles.sql: Sets up role-based access for PostgreSQL, granting only necessary permissions to each role for security.



---

Security and Optimization Highlights

1. Frontend Security

Secure Cookies: JWT tokens are stored in httponly, secure cookies to prevent client-side access.

Input Validation: All inputs are validated on both frontend and backend.

Error Handling: Centralized error handling in api/auth.js to provide user-friendly feedback.



2. Backend Security

JWT Authentication: Using app/utils/security.py to securely create and verify tokens, with JWT stored in httponly cookies.

Password Hashing: Securely hashing passwords using werkzeug.security.generate_password_hash.

Centralized Error Handling: app/error_handler.py intercepts all errors to provide consistent JSON responses.

Rate Limiting (Optional): Implement rate limiting middleware to prevent abuse, especially for critical endpoints.



3. Database Security

Role-Based Access Control: Only designated roles (e.g., gameuser) have permission to read/write to tables, minimizing risk.

SSL Enforcement: Configures PostgreSQL to enforce SSL for secure data transmission.

Indexes: Indexed columns (e.g., username and item_id) ensure quick retrieval, especially for marketplace data.



4. Docker Compose Setup (docker-compose.yml)

Defines services for frontend, backend, and database for easy deployment.

Sets up networked containers for secure, isolated communication between services.





---

Master README File

The root README.md provides high-level installation instructions, including Docker setup, .env configuration, and startup procedures for development and production.
