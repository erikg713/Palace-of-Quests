Palace of Quests (Pi Quest) is a Web3-enabled metaverse game that blends immersive gameplay with decentralized transactions. Built on the Pi Network, players can explore an evolving virtual world, level up their avatars, and earn in-game rewards. Future enhancements include cross-chain compatibility, bridging to Ethereum, and expansive questing across multiple networks.
---
Table of Contents
---
Features
Metaverse Gameplay: Progress from level 1 to 250, unlocking new challenges, quests, and storylines.
Rewards and Experience: Earn experience points and in-game currency to upgrade your avatar’s abilities and appearance.
Premium Subscription: Access all unlocked upgrades for $9.99/year.
Blockchain Integration: Seamlessly integrated with the Pi Network SDK (U2A) for secure, peer-to-peer payments.
Cross-Chain Compatibility (Planned): Connect to Ethereum and Tide networks for broader marketplace and questing opportunities.
Robust Database: Leveraging PostgreSQL for reliable data storage and efficient querying.
Clean, Scalable Code: Structured backend (Flask) and frontend (React) ensure maintainability and future-proofing.
---
Tech Stack
Frontend:
React (Web)
React Native (Future) for mobile platforms
Backend:
Flask (Python)
PostgreSQL Database
Blockchain:
Pi Network (Primary)
Ethereum (Planned)
Additional Tools:
JWT for authentication
Docker for containerization
CI/CD integrations (planned)
Testing frameworks (pytest, Jest) 
---

How It Works

1. Create an Account: Sign up using your Pi Network credentials.


2. Begin Your Journey: Start at level 1 and complete quests and challenges to gain rewards.


3. Avatar Upgrades: Spend earned rewards on new gear, abilities, and visual enhancements.


4. Go Premium: Unlock all in-game upgrades for a yearly subscription fee.


5. Secure Transactions: Use the Pi Network SDK for frictionless, decentralized, peer-to-peer payments.
---
---

*** Project Structure ***
palace-of-quests/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
│   ├── README.md
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── config.py
│   ├── models/
│   │   ├── database.py
│   │   ├── user.py
│   │   ├── quest.py
│   │   ├── marketplace_item.py
│
├── database/
│   ├── migrations.sql
│   ├── init.sql
│
├── README.md
---

Installation

Prerequisites

Python 3.10+

Node.js 18+

PostgreSQL 15+

Docker (Optional, for containerized deployment)


Backend Setup

1. Clone the repository:

git clone https://github.com/erikg713/palace-of-quests.git


2. Navigate to the backend directory:

cd palace-of-quests/backend


3. Install dependencies:

pip install -r requirements.txt


4. Run the development server:

flask run



Frontend Setup

1. Navigate to the frontend directory:

cd palace-of-quests/frontend


2. Install dependencies:

npm install


3. Start the React app:

npm start



Docker Setup

1. Build the Docker image:

docker-compose build


2. Run the application:

docker-compose up




---

Roadmap

[ ] MVP Launch: Initial release with Pi Network payment integration and core leveling system.

[ ] Expanded Levels & Features: Introduce new quests, challenges, and mini-games.

[ ] React Native Integration: Extend platform access to mobile devices.

[ ] Cross-Chain Functionality: Connect to Ethereum and Tide networks for broad interoperability.



---

Contributing

We welcome contributions! To get started:

1. Fork the repository.


2. Create a new branch:

git checkout -b feature-name


3. Commit your changes:

git commit -m "Add feature-name"


4. Push to your branch:

git push origin feature-name


5. Open a Pull Request against main.



For any major changes, please open an issue first to discuss what you would like to change.


---

License

This project is licensed under the Pi Network License. This license ensures compliance with the Pi Network's blockchain rules and protocols. For more details about this license, visit the official Pi Network documentation.


---

Contact

For questions, feedback, or support, please reach out via email:
piquests@gmail.com


---
