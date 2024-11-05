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
PalaceOfQuests/
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   │   ├── Avatar.js
│   │   │   ├── Inventory.js
│   │   │   ├── Quest.js
│   │   │   └── LevelUp.js
│   │   ├── pages/
│   │   │   ├── Home.js          # Main game hub
│   │   │   ├── QuestPage.js     # Quest list and details
│   │   │   ├── InventoryPage.js # Manage and equip items
│   │   │   └── ProfilePage.js   # Avatar customization and stats
│   │   └── styles/              # Styles for mobile and desktop
│   ├── public/
│   ├── .env.development
│   ├── .env.production
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── models.py            # Expanded models for items, quests, notifications
│   │   ├── routes/              # New routes for inventory, notifications
│   │   └── utils/               # Utilities for push notifications
│   ├── config.py
│   ├── .env.development
│   └── .env.production
│
└── README.md

Project Overview

The PiQuest structure is organized for a full-stack Web3 metaverse application with:

Frontend: React (with Three.js for 3D elements) optimized for mobile and Pi Network compatibility.

Backend: Flask API with JWT authentication, secure password hashing, and robust error handling.

Database: PostgreSQL with secure access control, structured for optimal performance with relational tables.


Unified Project Structure
PiQuest/
│
├── frontend/                  # React frontend
│   ├── src/
│   │   ├── api/               # API integration
│   │   ├── components/        # UI components
│   │   ├── pages/             # Page components (Home, Profile, Marketplace)
│   │   ├── App.js             # Main app component
│   │   ├── index.js           # React entry point
│   │   └── styles/            # Global and component-specific styles
│   ├── public/
│   └── package.json           # Frontend dependencies
│
├── backend/                   # Flask backend
│   ├── app/
│   │   ├── __init__.py        # App factory
│   │   ├── config.py          # Configurations (e.g., for database, JWT)
│   │   ├── models.py          # SQLAlchemy models
│   │   ├── routes/            # Blueprints (auth, marketplace, quests)
│   │   └── utils/             # Helper functions and utilities
│   ├── requirements.txt       # Backend dependencies
│   └── Dockerfile             # Backend Docker setup
│
├── database/
│   ├── schema.sql             # Database schema
│   └── roles.sql              # Role-based access configuration
│
├── .env.example               # Example environment variables file
├── docker-compose.yml         # Docker Compose setup
├── LICENSE                    # License file
└── README.md                  # Project overview and instructions
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


File: README.md (continued)

# PiQuest

**PiQuest** is a Web3 metaverse game built on the Pi Network, allowing users to sign in, participate in a marketplace, complete quests, and bridge assets with Tide Network and Ethereum.

## Project Structure

PiQuest/ ├── frontend/                  # React frontend ├── backend/                   # Flask backend ├── database/                  # Database schema and roles ├── docker-compose.yml         # Docker Compose setup └── README.md                  # Project overview and instructions

## Features

- **User Authentication**: Sign in with Pi Network.
- **Marketplace**: Buy and sell items.
- **Quests**: Complete in-game tasks for rewards.
- **Cross-Chain**: Interact with Tide Network and Ethereum.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/piquest.git

2. Setup Frontend

Navigate to the frontend directory, install dependencies, and start the application:

cd frontend
npm install
npm start


3. Setup Backend

Navigate to the backend directory, install dependencies, and start the Flask app:

cd backend
pip install -r requirements.txt
flask run


4. Initialize Database

Navigate to the database directory and run SQL scripts to set up the database schema and roles:

cd database
psql -U postgres -d piquest_db -f schema.sql
psql -U postgres -d piquest_db -f roles.sql


5. Run with Docker Compose

To start all services (frontend, backend, and database) using Docker Compose, use:

docker-compose up --build -d



Environment Variables

Create .env files in both the frontend and backend directories with the following settings:

.env for Backend

DATABASE_URL=postgresql://gameuser:your_secure_password@database/piquest_db
JWT_SECRET_KEY=your_jwt_secret_key
PI_API_KEY=your_pi_api_key

.env for Frontend

REACT_APP_BACKEND_URL=http://localhost:5000

Running Tests

PiQuest uses Cypress for end-to-end (E2E) testing, covering the authentication and payment flows.

Setting Up Cypress

1. Install Cypress in the frontend directory:

cd frontend
npm install cypress --save-dev


2. Run Cypress Tests:

Interactive Mode:

npx cypress open

Headless Mode (for CI/CD pipelines):

npx cypress run




Test Scenarios

Authentication: Verifies successful and failed user sign-ins.

Payment Flow: Tests payment lifecycle (approval, completion, cancellation).

Error Handling: Simulates various error scenarios to ensure proper user feedback.


Deployment

Using Docker Compose for Deployment

1. Prepare Environment Variables: Ensure .env files contain the correct production values.


2. Build and Start the Application:

docker-compose up --build -d



Production Deployment

Frontend: Deploy the static build of the frontend (e.g., Vercel or Netlify).

Backend: Use a cloud provider for backend deployment (e.g., AWS, Heroku, or DigitalOcean).

Database: Host the database using a managed PostgreSQL service.


CI/CD Integration

Integrate Cypress tests into your CI/CD pipeline (e.g., GitHub Actions, GitLab CI).

Use environment variables to manage secrets and configuration across environments (e.g., .env.production).


Security Considerations

1. JWT and Cookie Security: Use httponly and secure flags on cookies to store JWTs, protecting them from JavaScript access and ensuring HTTPS-only transmission.


2. Database Access Restrictions: Limit database access with roles (e.g., gameuser) to prevent unauthorized access.


3. Environment Variables: Keep sensitive keys like PI_API_KEY in environment variables and avoid hardcoding them.


4. Content Security Policy (CSP): Implement CSP headers to restrict content sources, mitigating XSS attacks.


5. SSL/TLS: Enforce HTTPS to secure data in transit between clients and servers.



Contributing

We welcome contributions to PiQuest! Here’s how to get started:

1. Fork the repository.


2. Create a branch for your feature or bugfix: git checkout -b feature-name.


3. Commit your changes and push the branch.


4. Create a Pull Request to the main branch.



Code Style Guidelines

Python: Follow PEP 8 for Python code style.

JavaScript: Use ESLint recommendations for JavaScript.

SQL: Use uppercase for SQL keywords and lowercase for table/column names.


License

This project is licensed under the MIT License. See the LICENSE file for details.



4. Docker Compose Setup (docker-compose.yml)

Defines services for frontend, backend, and database for easy deployment.

Sets up networked containers for secure, isolated communication between services.





---

Master README File

The root README.md provides high-level installation instructions, including Docker setup, .env configuration, and startup procedures for development and production.
