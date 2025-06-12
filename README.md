---

# Palace of Quests (Pi Quest) 🏰

**Palace of Quests** is an immersive, Web3-powered metaverse adventure built on the Pi Network. Explore a dynamic world, complete quests, level up, and earn real rewards—powered by blockchain technology and a vibrant community.

[![Build Status](https://img.shields.io/github/actions/workflow/status/erikg713/Palace-of-Quests/main.yml?branch=main)](https://github.com/erikg713/Palace-of-Quests/actions)
[![License](https://img.shields.io/github/license/erikg713/Palace-of-Quests)](LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

Palace of Quests is designed for players seeking a next-generation gaming experience where gameplay, real-world value, and community converge. Built with modern web technologies and Pi Network integration, the platform offers:

- **A living, evolving metaverse** where every quest counts
- **True Web3 ownership** of in-game assets and rewards
- **A fair, secure, and transparent ecosystem** for all participants

---

## Features

- 🌍 **Dynamic Metaverse:** Rich, explorable worlds with evolving quests and challenges.
- 🏆 **Earn-as-You-Play:** Complete quests to earn Pi Network rewards and unlock new abilities.
- 🔗 **Web3 Integration:** Secure, decentralized transactions and authentication via Pi Network SDK.
- 🎮 **Level Up Progression:** Enhance your character and access new areas and features.
- 🤝 **Multiplayer & Community:** Play solo or team up with friends in real time.
- 🛡️ **Robust Security:** JWT authentication, secure payments, and best practices throughout.
- 💬 **Active Community:** Join a growing network of players, creators, and contributors.

---

## Screenshots

<!--
Add real screenshots or GIFs to showcase your game. Example:
![Game Lobby](assets/screenshot-lobby.png)
![Quest Map](assets/screenshot-questmap.gif)
-->

---

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 16+ and npm
- PostgreSQL 13+
- Docker (optional but recommended for deployment)

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
cp .env.example .env  # Edit with your credentials and secrets

# Database setup (see database/README.md for full details)
createdb piquest_db
psql -U <your_user> -d piquest_db -f ../database/schema.sql
psql -U <your_user> -d piquest_db -f ../database/roles.sql

# Frontend setup
cd ../frontend
npm install
```

*For more advanced setup and Docker deployment, see [backend/README.md](backend/README.md) and [database/README.md](database/README.md).*

---

## Usage

```bash
# Start backend (from backend/)
flask run

# Start frontend (from frontend/)
npm start
```

Open [http://localhost:3000](http://localhost:3000) in your browser to play.

---

## Technologies Used

- **Python (Flask):** Backend API, authentication, business logic
- **JavaScript & TypeScript (React):** Frontend UI and client logic
- **PostgreSQL:** Persistent, reliable game data storage
- **CSS:** Responsive, modern styles
- **Docker:** Effortless local and cloud deployment
- **Pi Network SDK:** Web3 transactions, authentication, and rewards

---

## Contributing

We welcome contributions from developers, artists, and enthusiasts!

1. Fork this repository and create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
2. Make your changes and commit them with clear, descriptive messages.
3. Push your branch and open a Pull Request.
4. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## License

This project is licensed under the PIOS License. See [LICENSE](LICENSE) for full details.

---

## Contact

For questions, suggestions, or feedback, reach out at:  
📧 **piquests@gmail.com**

Or connect on [GitHub](https://github.com/erikg713/Palace-of-Quests).

---

Ready to forge your destiny? Join Palace of Quests and help shape the next era of metaverse gaming!

---
