-- roles.sql
CREATE ROLE gameuser LOGIN PASSWORD 'your_secure_password';
GRANT CONNECT ON DATABASE piquest_db TO gameuser;

-- Grant SELECT, INSERT, and UPDATE permissions on all tables to the `gameuser` role.
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO gameuser;
