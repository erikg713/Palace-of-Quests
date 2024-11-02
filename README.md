PiQuest Project Structure

Project Overview

The PiQuest structure is organized for a full-stack Web3 metaverse application with:

Frontend: React (with Three.js for 3D elements) optimized for mobile and Pi Network compatibility.

Backend: Flask API with JWT authentication, secure password hashing, and robust error handling.

Database: PostgreSQL with secure access control, structured for optimal performance with relational tables.
**Project Structure**
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

