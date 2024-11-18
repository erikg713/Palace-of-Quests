Palace of Quests

Palace of Quests is a Web3-based metaverse and marketplace built on the Pi Network. The platform integrates blockchain for secure payments, user authentication, and a gamified experience. The app features a marketplace for digital goods, quests, and interactions with the Pi Network. The future will bring additional multi-chain support (Ethereum, Polygon, Bitcoin) through cross-chain bridges.


---

Features

Marketplace: A platform where users can buy and sell digital assets using Pi coins, with plans to integrate Ethereum, Polygon, and Bitcoin.

Gamified Quests: Users can embark on quests to earn rewards.

Pi Network Payment Integration: Handles secure transactions and user login through Pi coins.

Cross-Chain Bridges: Future plans for integrating Ethereum, Polygon, and Bitcoin for broader payment options.

Web3 Metaverse: A digital world that integrates blockchain and virtual experiences.

Backend with Flask and PostgreSQL: Scalable architecture with a secure database setup.

Dockerized Deployment: Simplified containerization for both frontend and backend services.



---

Project Structure

The project consists of two main components:

1. Frontend (React)

Built with React for dynamic, responsive UI.

Integrates Pi Network SDK for Pi coin authentication and payments.

Uses environment variables to differentiate between development, staging, and production environments.

Docker-ready for containerized deployments.


2. Backend (Flask)

Flask serves as the backend framework for handling API requests.

PostgreSQL is used for managing user data, transactions, and marketplace items.

The backend integrates the Pi Network SDK for secure Pi coin transactions.

The backend is also Dockerized for easy deployment.



---

Setup

Prerequisites

Node.js (v16+ recommended) for the frontend.

Python 3.9+ for the backend.

PostgreSQL database instance for the backend.

Docker (optional but recommended).

Pi Network App Credentials from the Pi Developer Portal.



---

Installation

1. Frontend Setup

1. Clone the repository:

git clone https://github.com/your-repo/palace-of-quests-frontend.git
cd palace-of-quests-frontend


2. Install dependencies:

npm install


3. Set up the .env file with Pi Network credentials and backend URL:

REACT_APP_BACKEND_URL=http://localhost:5000
REACT_APP_PI_APP_ID=your_pi_app_id
REACT_APP_PI_API_KEY=your_pi_api_key
REACT_APP_PI_ENV=development


4. Start the development server:

npm start



2. Backend Setup

1. Clone the repository:

git clone https://github.com/your-repo/palace-of-quests-backend.git
cd palace-of-quests-backend


2. Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


4. Configure the .env file with the required keys:

FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://user:password@localhost:5432/palace_of_quests
PI_APP_ID=your_pi_app_id
PI_API_KEY=your_pi_api_key


5. Run migrations for PostgreSQL:

flask db upgrade


6. Start the backend server:

flask run



3. Docker Setup (Optional)

1. Build the Docker images for both frontend and backend:

docker build -t palace-of-quests-frontend ./frontend
docker build -t palace-of-quests-backend ./backend


2. Run the containers:

docker run -p 3000:3000 palace-of-quests-frontend
docker run -p 5000:5000 palace-of-quests-backend




---

API Endpoints

Authentication

POST /auth/register: Register a new user.

POST /auth/login: Authenticate the user and receive a JWT token.


Payments

POST /payment/initiate: Initiate a Pi coin transaction.

POST /payment/complete: Complete the Pi coin transaction.


Marketplace

GET /marketplace: Retrieve a list of marketplace items.

POST /marketplace: Add a new item to the marketplace.


Quests

GET /quests: Retrieve available quests.

POST /quests: Create a new quest.



---

Deployment

Hosting

This backend and frontend can be deployed on popular hosting services like:

AWS EC2, Heroku, DigitalOcean, Netlify (for frontend).

PostgreSQL can be hosted on platforms like ElephantSQL or AWS RDS.


Make sure to configure environment variables on your hosting platform to match the local .env files.


---

Contributing

We welcome contributions! To contribute:

1. Fork the repository.


2. Create a new feature branch:

git checkout -b feature/your-feature


3. Commit your changes and push to the branch.


4. Open a pull request.




---

License

This project is licensed under the MIT License. See the LICENSE file for more details.


---

Let me know if you need any other details or specific adjustments!

