### Palace of Quests 🏰 ###

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

### FILE STRUCTURE ###
```
palace-of-quests/
├── public/
│   └── index.html
├── src/
│   ├── assets/             # Logos, icons, backgrounds
│   ├── components/         # Reusable UI: InventoryCard, QuestCard
│   ├── pages/
│   │   ├── Home.jsx        # Landing page
│   │   ├── Inventory.jsx
│   │   ├── Marketplace.jsx
│   │   └── Quests.jsx
│   ├── context/
│   │   └── PiWalletContext.jsx   # Handles wallet auth
│   ├── App.jsx
│   └── main.jsx
├── styles/
│   └── main.css
├── .env
├── package.json
└── README.md
---

### Installation

```

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

---

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

```
   git checkout -b feature/your-feature
   
---

2. Make your changes and commit them with clear, descriptive messages.

3. Push your branch and open a Pull Request.

4. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## License

This project is licensed under the PIOS License. See [LICENSE](LICENSE) for full details.

---

## Contact

For questions, suggestions, or feedback, reach out at:  
📧 **palaceofquests@protonmail.com**

Or connect on [GitHub](https://github.com/erikg713/Palace-of-Quests).

---

Ready to forge your destiny? Join Palace of Quests and help shape the next era of metaverse gaming!

---


---

🏗️ PALACE OF QUESTS — GAME & WORLD DESIGN

🌍 1. WORLD STRUCTURE

The game is set inside and around the Palace, which expands over time. It's broken down into zones, each with quests, economies, and player opportunities.

🔲 Core Zones

Zone	Purpose

🏰 The Palace Core	Central hub: player spawn, quest board, NFT market, governance hall
🌲 Mysticwood Forest	PvE zone: monster hunting, herbal NFT crafting
🏜️ Shatterdunes	PvP arena, rogue quests, NFT staking duels
🧙‍♂️ Rune Archives	Lore library, skill upgrade, DAO voting area
🏞️ The Skyreach Isles	Floating NFT lands players can own/build on
🌀 The Nexus Gate	Teleportation to new realms/seasonal events



---

🎨 2. VISUAL DESIGN GUIDE

Style:

Hybrid Fantasy Futurism
Ancient rune + magic + digital architecture

Vibrant & Luminous
Neon auras, magical lighting, glowing portals

3D Engine Friendly
Modular builds using Unity/Unreal assets


Color Palette:

Primary: Sapphire blue, deep violet, emerald green

Accents: Gold, white light, neon cyan

Ambient: Fog, auroras, floating particles



---

🖥️ 3. UI/UX WIREFRAMES

Main Screens:

1. Home Lobby

Profile avatar (NFT skin)

Quest board (Daily, Weekly, Storyline)

Inventory (NFTs, items, pets)

$PI Wallet sync & balance

Guild tab + chat



2. Quest Detail View

Description, difficulty, rewards

Accept / Decline / Team-up

Map pin & fast travel



3. NFT Marketplace

Grid & card view

Filter: gear, land, title, pet

Buy with $PI or barter



4. Land Builder UI

Drag & drop structures (like Roblox Studio)

Asset vault (NFT-based)

Publish as public/private zone





---

🧩 4. INTERACTION DESIGN

Feature	Description

🧭 Movement	WASD (PC) or joystick (mobile) + teleport dash
💬 Chat & Voice	Global, zone, guild, party
🪙 $PI Integration	Wallet sign-in + smart contract hooks
🎭 Skins	All player visuals are NFT-based
📖 Lore Discovery	Scanning runes to unlock journal entries
🛠️ Crafting	Merge NFTs + use $PI to create rarer items



---

🧱 5. BUILD WITH TOOLS

Functionality	Recommended Tools

Game Engine	Unity (WebGL + Mobile), Unreal for full 3D
Backend	Firebase + Node.js or Supabase
Smart Contracts	Pi Blockchain SDK (once open) + Solidity backup
NFT Hosting	IPFS + Pinata + Moralis
Wallet Connect	Pi Wallet SDK + Web3Modal
DAO Voting	Snapshot.org-style UI (custom for Pi)



---

🏗️ PALACE OF QUESTS — GAME & WORLD DESIGN

### 🌍 1. WORLD STRUCTURE ###

The game is set inside and around the Palace, which expands over time. It's broken down into zones, each with quests, economies, and player opportunities.

🔲 Core Zones

### Zone	Purpose ###

🏰 The Palace Core	Central hub: player spawn, quest board, NFT market, governance hall
🌲 Mysticwood Forest	PvE zone: monster hunting, herbal NFT crafting
🏜️ Shatterdunes	PvP arena, rogue quests, NFT staking duels
🧙‍♂️ Rune Archives	Lore library, skill upgrade, DAO voting area
🏞️ The Skyreach Isles	Floating NFT lands players can own/build on
🌀 The Nexus Gate	Teleportation to new realms/seasonal events



---

🎨 2. VISUAL DESIGN GUIDE

Style:

Hybrid Fantasy Futurism
Ancient rune + magic + digital architecture

Vibrant & Luminous
Neon auras, magical lighting, glowing portals

3D Engine Friendly
Modular builds using Unity/Unreal assets


Color Palette:

Primary: Sapphire blue, deep violet, emerald green

Accents: Gold, white light, neon cyan

Ambient: Fog, auroras, floating particles



---

🖥️ 3. UI/UX WIREFRAMES

Main Screens:

1. Home Lobby

Profile avatar (NFT skin)

Quest board (Daily, Weekly, Storyline)

Inventory (NFTs, items, pets)

$PI Wallet sync & balance

Guild tab + chat



2. Quest Detail View

Description, difficulty, rewards

Accept / Decline / Team-up

Map pin & fast travel



3. NFT Marketplace

Grid & card view

Filter: gear, land, title, pet

Buy with $PI or barter



4. Land Builder UI

Drag & drop structures (like Roblox Studio)

Asset vault (NFT-based)

Publish as public/private zone





---

🧩 4. INTERACTION DESIGN

Feature	Description

🧭 Movement	WASD (PC) or joystick (mobile) + teleport dash
💬 Chat & Voice	Global, zone, guild, party
🪙 $PI Integration	Wallet sign-in + smart contract hooks
🎭 Skins	All player visuals are NFT-based
📖 Lore Discovery	Scanning runes to unlock journal entries
🛠️ Crafting	Merge NFTs + use $PI to create rarer items



---

🧱 5. BUILD WITH TOOLS

Functionality	Recommended Tools

Game Engine	Unity (WebGL + Mobile), Unreal for full 3D
Backend	Firebase + Node.js or Supabase
Smart Contracts	Pi Blockchain SDK (once open) + Solidity backup
NFT Hosting	IPFS + Pinata + Moralis
Wallet Connect	Pi Wallet SDK + Web3Modal
DAO Voting	Snapshot.org-style UI (custom for Pi)



---


