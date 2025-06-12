---

# Palace of Quests (Pi Quest) 🏰

**Palace of Quests** is a Web3-powered metaverse game built on the Pi Network. Explore an immersive world, level up, complete quests, and earn real rewards—all powered by next-generation blockchain technology.

[![Build Status](https://img.shields.io/github/actions/workflow/status/erikg713/Palace-of-Quests/main.yml?branch=main)](https://github.com/erikg713/Palace-of-Quests/actions)
[![License](https://img.shields.io/github/license/erikg713/Palace-of-Quests)](LICENSE)

---

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- 🌍 **Dynamic Metaverse**: Explore a rich, evolving world full of Pi-powered quests.
- 🏆 **Earn-as-You-Play**: Gain real Pi rewards for accomplishing in-game challenges.
- 🔗 **Web3 Integration**: Secure decentralized transactions via Pi Network.
- 🎮 **Progression System**: Level up, unlock abilities, and customize your avatar.
- 🤝 **Multiplayer**: Play, trade, and complete quests with friends or rivals.
- 🛡️ **Secure Auth**: Modern authentication with JWT and Pi Network SDK.
- 💬 **Active Community**: Engage with a growing community of questers.

---

## Screenshots

<!-- Insert GIFs or screenshots here for best results. Example below: -->
<!-- ![Screenshot of Palace of Quests gameplay](assets/screenshot1.png) -->

---

## Getting Started

### Prerequisites

- **Python** 3.9+
- **Node.js** 16+ and **npm**
- **PostgreSQL** 13+
- **Docker** (optional, for containerization)

### Installation

```bash
# Clone the repository
git clone https://github.com/erikg713/Palace-of-Quests.git
cd Palace-of-Quests

# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Fill in your secrets

# Database setup
# (see database/README.md for schema and roles)
createdb piquest_db
psql -U <your_user> -d piquest_db -f ../database/schema.sql
psql -U <your_user> -d piquest_db -f ../database/roles.sql

# Frontend setup
cd ../frontend
npm install
```

*For full setup details and Docker instructions, see [backend/README.md](backend/README.md) and [database/README.md](database/README.md).*

---

## Usage

```bash
# Start backend (from backend/)
flask run

# Start frontend (from frontend/)
npm start
```

Visit [http://localhost:3000](http://localhost:3000) in your browser.

---

## Technologies Used

- **Python** (Flask) — Backend API & game logic
- **JavaScript / TypeScript** — Frontend (React)
- **PostgreSQL** — Persistent game data
- **CSS** — Styling and UI
- **Docker** — Containerization and easy deployment
- **Pi Network SDK** — Web3 and payment integration

---

## Contributing

We're excited to welcome new contributors! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repo and create your branch:  
   `git checkout -b feature/your-feature`
2. Commit your changes and push:  
   `git push origin feature/your-feature`
3. Open a Pull Request and describe your changes.

---

## License

This project is licensed under the PIOS License. See [LICENSE](LICENSE) for details.

---

## Contact

Questions or suggestions?  
📧 **piquests@gmail.com**

[GitHub Repository](https://github.com/erikg713/Palace-of-Quests)

---

**Ready to embark on your quest? Join us and build the future of metaverse gaming!**

---
