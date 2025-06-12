Palace of Quests Backend

This is the backend service for Palace of Quests, a Web3 application integrating the Pi Network SDK to enable secure transactions and user authentication. It is built with Flask and supports PostgreSQL as the database.
mkdir backend && cd backend
python -m venv venv
source venv/bin/activate
pip install flask flask-cors flask-restful

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Development](#development)
- [API Endpoints](#api-endpoints)
- [Docker Deployment](#docker-deployment)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
---

Features

RESTful API: Provides endpoints for frontend interaction.

JWT Authentication: Ensures secure user sessions.

Pi Network Payment Integration: Handles Pi coin transactions via the Pi Network SDK.

PostgreSQL Support: Robust database for data storage.

Dockerized Deployment: Simplifies environment setup and scaling.



---

Prerequisites

Before setting up the backend, ensure you have the following:

Python: v3.9+ installed.

PostgreSQL: Database instance running.

Docker: Optional but recommended for containerized deployment.

Pi Network App credentials from the Pi Developer Portal.



---

Installation

1. Clone the Repository:

git clone https://github.com/your-repo/palace-of-quests-backend.git
cd palace-of-quests-backend


2. Create a Virtual Environment:

python3 -m venv venv
source venv/bin/activate


3. Install Dependencies:

pip install -r requirements.txt


4. Set Up the .env File: Create a .env file in the root directory with the following keys:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_random_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/palace_of_quests
PI_APP_ID=your_pi_app_id
PI_API_KEY=your_pi_api_key

Replace placeholders with your actual configuration.


5. Initialize the Database: Run migrations to set up the database schema:

flask db upgrade




---

Development

1. Run the Development Server:

flask run

The server will start at http://localhost:5000.


2. Testing Endpoints: Use tools like Postman or cURL to interact with the API.




---

API Endpoints

Authentication

POST /auth/register: Register a new user.

POST /auth/login: Authenticate and return a JWT.


Payments

POST /payment/initiate: Start a Pi coin transaction.

POST /payment/complete: Confirm a transaction.


Quests

GET /quests: Fetch all quests.

POST /quests: Add a new quest.



---

Docker Deployment

1. Build the Docker Image:

docker build -t palace-of-quests-backend .


2. Run the Container:

docker run -p 5000:5000 --env-file .env palace-of-quests-backend


3. Using Docker-Compose: If you have a docker-compose.yml file, start the service:

docker-compose up




---

Deployment

Hosting Platforms

The backend can be deployed on platforms like:

AWS EC2 or Lightsail

Heroku

Google Cloud

DigitalOcean


Ensure you set the environment variables on the hosting platform to match your .env file.


---

Contributing

1. Fork the repository.


2. Create a new branch:

git checkout -b feature/your-feature


3. Commit your changes and push to the branch.


4. Open a pull request.


backend/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── player.py
│   │   ├── challenges.py
│   │   ├── marketplace.py
│   │   ├── payments.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── jwt_utils.py
│   │   ├── pi_network_sdk.py
│   └── config.py
├── migrations/
├── tests/
│   ├── test_auth.py
│   ├── test_player.py
│   ├── test_marketplace.py
├── wsgi.py
├── requirements.txt
└── run.py
---

License

This project is licensed under the MIT License.


---

Feel free to ask for adjustments or more advanced sections like testing, monitoring, or CI/CD!

Great! Since you requested professional, human-like rewrites and optimizations for all README/documentation parts (and potentially for code files too), here’s how I’ll proceed:

**Step 1:** I’ll rewrite and optimize all documentation-related files (`README.md` in the root, `backend/README.md`, `database/README.md`).  
**Step 2:** If you want code file reviews or improvements, let me know which file or area to start with.

Below are rewritten versions for your main documentation files. Each is concise, inviting, and clear—reflecting best open source practices and the professionalism of a human developer.

---

## Root `README.md`

```markdown
# Palace of Quests (Pi Quest) 🏰

_An immersive Web3 metaverse adventure powered by the Pi Network. Explore, quest, and earn real rewards in a dynamic virtual world._

[![Build Status](https://img.shields.io/github/actions/workflow/status/erikg713/Palace-of-Quests/main.yml?branch=main)](https://github.com/erikg713/Palace-of-Quests/actions)
[![License](https://img.shields.io/github/license/erikg713/Palace-of-Quests)](LICENSE)

---

## Overview

Palace of Quests is a next-generation multiplayer metaverse experience. Complete quests, level up, collect rewards, and shape a living world—integrated seamlessly with Web3 and the Pi Network.

---

## Features

- 🌍 Expansive, evolving world of quests and challenges
- 🏆 Real Pi rewards for gameplay achievements
- 🔗 Web3 & Pi Network integration for secure, decentralized transactions
- 🎮 Progression system and unlockable abilities
- 🤝 Multiplayer: Collaborate, compete, and trade with players worldwide

---

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+ & npm
- PostgreSQL 13+
- Docker (optional, for deployment)

### Setup

```bash
git clone https://github.com/erikg713/Palace-of-Quests.git
cd Palace-of-Quests

# Backend
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # Update secrets

# Database
createdb piquest_db
psql -U <user> -d piquest_db -f ../database/schema.sql
psql -U <user> -d piquest_db -f ../database/roles.sql

# Frontend
cd ../frontend
npm install
```

---

## Usage

```bash
# Backend
flask run

# Frontend
npm start
```

Visit [http://localhost:3000](http://localhost:3000).

---

## Technologies

- **Backend:** Python (Flask)
- **Frontend:** JavaScript/TypeScript (React)
- **Database:** PostgreSQL
- **Web3:** Pi Network SDK
- **Containerization:** Docker

---

## Contributing

We welcome improvements and ideas! See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

Licensed under PIOS. See [LICENSE](LICENSE).

---

## Contact

Questions or suggestions?  
📧 piquests@gmail.com  
[GitHub Repo](https://github.com/erikg713/Palace-of-Quests)

---

_Ready for your quest? Join us and help shape the metaverse!_
```

---

## `backend/README.md`

```markdown
# Palace of Quests Backend

The backend service for Palace of Quests, built with Flask and PostgreSQL, integrates the Pi Network SDK for secure payments and user authentication.

---

## Features

- RESTful API for game logic and frontend integration
- JWT-based secure authentication
- Seamless Pi Network payment handling
- Full PostgreSQL support
- Dockerized for easy deployment

---

## Requirements

- Python 3.9+
- PostgreSQL
- Docker (optional)

---

## Setup

```bash
git clone https://github.com/erikg713/Palace-of-Quests.git
cd Palace-of-Quests/backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # Edit credentials

# Database migration
flask db upgrade
```

---

## Running Locally

```bash
flask run
```

Server runs at [http://localhost:5000](http://localhost:5000).

---

## API Endpoints

**Auth**
- `POST /auth/register` — Register user
- `POST /auth/login` — Login, returns JWT

**Payments**
- `POST /payment/initiate` — Start Pi payment
- `POST /payment/complete` — Finalize payment

**Quests**
- `GET /quests` — List all quests
- `POST /quests` — Create quest

---

## Docker

```bash
docker build -t palace-of-quests-backend .
docker run -p 5000:5000 --env-file .env palace-of-quests-backend
```

Or with Compose:

```bash
docker-compose up
```

---

## Contributing

1. Fork and branch:  
   `git checkout -b feature/your-feature`
2. Commit & push  
3. Open a Pull Request

---

## License

MIT License (see [LICENSE](../LICENSE)).
```

---

## `database/README.md`

```markdown
# Palace of Quests Database

PostgreSQL setup for Palace of Quests.

---

## Setup

1. **Ensure PostgreSQL is running**  
   Use Docker Compose or your local Postgres installation.

2. **Create the Database**

```bash
createdb piquest_db
```

3. **Run Schema & Role Scripts**

```bash
psql -U <user> -d piquest_db -f database/schema.sql
psql -U <user> -d piquest_db -f database/roles.sql
```

4. **Configure Environment**

Set database credentials in your `backend/.env` file:

```
DATABASE_URL=postgresql://gameuser:your_secure_password@localhost/piquest_db
JWT_SECRET_KEY=your_jwt_secret_key
```

---

## Docker Compose

If using Docker Compose, the database will initialize automatically.

---

## Tips

- Update credentials and secrets before deploying.
- For schema changes, update `schema.sql` and use migrations.

---

_Questions? See the main project README or contact us._
```

---

Let me know if you want specific code files reviewed or refactored next—just name the file or area!
