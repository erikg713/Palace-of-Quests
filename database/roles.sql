-- Create gameuser role with login
CREATE ROLE gameuser LOGIN PASSWORD 'secure_password';
GRANT CONNECT ON DATABASE piquest_db TO gameuser;

-- Grant role access only to necessary tables
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO gameuser;
