# Palace of Quests (Pi Quest)

**Palace of Quests (Pi Quest)** is a Web3-enabled metaverse game that blends immersive gameplay with decentralized transactions. Built on the Pi Network, players can explore an evolving virtual world, level up their avatars, and earn in-game rewards. Future enhancements include cross-chain compatibility, bridging to Ethereum, and expansive questing across multiple networks.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Docker Setup](#docker-setup)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Metaverse Gameplay:** Progress from level 1 to 250, unlocking new challenges, quests, and storylines.
- **Rewards and Experience:** Earn experience points and in-game currency to upgrade your avatar’s abilities and appearance.
- **Premium Subscription:** Access all unlocked upgrades for $9.99/year.
- **Blockchain Integration:** Seamlessly integrated with the Pi Network SDK (U2A) for secure, peer-to-peer payments.
- **Cross-Chain Compatibility (Planned):** Connect to Ethereum and Tide networks for a broader marketplace and questing opportunities.
- **Robust Database:** Leveraging PostgreSQL for reliable data storage and efficient querying.
- **Clean, Scalable Code:** Structured backend (Flask) and frontend (React) ensure maintainability and future-proofing.

---

## Tech Stack

**Frontend:**
- React (Web)
- React Native *(Future)* for mobile platforms

**Backend:**
- Flask (Python)
- PostgreSQL Database

**Blockchain:**
- Pi Network (Primary)
- Ethereum *(Planned)*

**Additional Tools:**
- JWT for authentication
- Docker for containerization
- CI/CD integrations *(planned)*
- Testing frameworks: `pytest`, `Jest`

---

## Project Structure

```
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
```

---

## Installation

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 15+
- Docker (Optional)
- Pi Network SDK (U2A)
- `pip install selenium webdriver-manager`
- `npx react-native init PalaceOfQuestsMobile`
- `cd PalaceOfQuestsMobile`
- `npm install axios react-navigation react-native-async-storage`
- `npm install --save-dev jest @testing-library/react @testing-library/jest-dom @testing-library/user-event`

### Backend Setup

```bash
mkdir backend && cd backend
python -m venv venv
source venv/bin/activate  # Activate virtual environment
pip install flask flask-sqlalchemy flask-migrate flask-jwt-extended flask-cors
```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd palace-of-quests/frontend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Start the React app:
    ```bash
    npm start
    ```

---

## Docker Setup

1. **Build the Docker image:**
    ```bash
    docker-compose build
    ```
2. **Run the application:**
    ```bash
    docker-compose up
    flask db init        # Initialize migrations folder
    flask db migrate -m "Initial migration"
    flask db upgrade     # Apply migrations to the database
    ```

---

## Roadmap

- [ ] **MVP Launch:** Initial release with Pi Network payment integration and core leveling system.
- [ ] **Expanded Levels & Features:** Introduce new quests, challenges, and mini-games.
- [ ] **React Native Integration:** Extend platform access to mobile devices.
- [ ] **Cross-Chain Functionality:** Connect to Ethereum and Tide networks for broad interoperability.

---

## Contributing

We welcome contributions! To get started:

1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature-name
    ```
3. **Commit your changes:**
    ```bash
    git commit -m "Add feature-name"
    ```
4. **Push to your branch:**
    ```bash
    git push origin feature-name
    ```
5. **Open a Pull Request** against `main`.

For any major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the **Pi Network License**. This license ensures compliance with the Pi Network's blockchain rules and protocols.  
For more details, visit the official Pi Network documentation.

---

## Contact

For questions, feedback, or support, please reach out via email:  
📧 **piquests@gmail.com**

[GitHub Repository](https://github.com/erikg713/Palace-of-Quests.git)
