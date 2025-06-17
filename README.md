---

🎮 What It Is

Palace of Quests is a Web3-enabled metaverse adventure built on the Pi Network. Players explore zones, complete quests, level up avatars, trade NFTs, and earn Pi tokens through secure, decentralized transactions .


---

🛠 Key Features

Dynamic Metaverse: Evolving world with zones like Mysticwood Forest (PvE), Shatterdunes (PvP), Skyreach Isles (land ownership), and more.

Earn-as-You-Play: Complete quests to gain Pi rewards, items, and abilities.

Web3 Integration: Pi Network SDK handles authentication and crypto payments.

NFT Ecosystem: Players own, trade, and craft NFTs (gear, pets, land, titles).

Multiplayer Community: Team quests, guilds, chat, and voice integration.

Secure Architecture: JWT auth, blockchain-backed transactions, designed for fairness.

DAO/Governance: In-app real-time voting zones like Rune Archives.

Crafting & Skins: Merge NFTs, customize avatars—merge gameplay with creative expression.



---

⚙️ Tech Stack & Structure

Backend:

Python (Flask) for APIs, game logic, authentication

PostgreSQL for persistent data

Docker-supported deployment


Frontend:

React (JS/TS) for UI (Quests, Inventory, Marketplace pages)

Pi Wallet integration via context/provider

Mobile-ready (future React Native support)


Dev Environment:

1. Clone the repo


2. Backend: Python 3.9+ + pip install, .env, PostgreSQL 13+, run schema/roles SQL


3. Frontend: Node 16+, npm install


4. Optionally use Docker (docker-compose.yml) for full-stack setup  




---

🏗 Gameplay & World Design

Zones & Purpose

Palace Core: Spawn point, quest board, NFT market, governance

Mysticwood Forest: PvE, crafting

Shatterdunes: PvP duels, NFT staking

Rune Archives: Lore, skill upgrades, DAO voting

Skyreach Isles: Player-owned land

Nexus Gate: Seasonal/expandable realms


Visual Style: Fantasy-futuristic, modular for 3D engines, vibrant neon/rune ambiance

UI Screens: Lobby (wallet, inventory, chat), Quest Detail, Marketplace, Land Builder

Controls: WASD + teleport/mobile joystick, global/zone/guild chat, voice



---

🧱 Tools & Systems

Engines: Unity (WebGL/mobile) or Unreal

Infrastructure: Firebase/Supabase backend possible

Blockchain: Pi SDK (primary), with Solidity + cross-chain ambitions (Ethereum, Tide)

NFT Storage: IPFS, Pinata, Moralis

Wallet Connect: Pi Wallet SDK (plus Web3Modal)

DAO Governance: Snapshot-style voting UIs



---

🔄 Getting Started

git clone https://github.com/erikg713/Palace-of-Quests.git
cd Palace-of-Quests/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # configure DB, Pi SDK, secrets

# Set up Postgres DB:
createdb piquest_db
psql -U <user> -d piquest_db -f ../database/schema.sql
psql -U <user> -d piquest_db -f ../database/roles.sql

# Frontend
cd ../frontend
npm install

Run backend: flask run (default localhost:5000)

Run frontend: npm start (default localhost:3000)

Visit http://localhost:3000 to play 



---

👥 Contributors & Community

Open-source, encouraging developer and creator contributions

Use GitHub flow (fork → branch → PR), see CONTRIBUTING.md

Licensed under the PIOS License


Contact via palaceofquests@protonmail.com or the GitHub repository  


---

✅ Summary

Palace of Quests is a full-stack Web3 metaverse built on Pi Network with crypto-rewards, NFT ownership, DAO-style governance, and modular game world expansion in mind. It’s ideal for blockchain game devs, Web3 explorers, and community contributors looking to engage deeply with a next-gen gaming ecosystem.


---

If you'd like help digging into database schemas (schema.sql, roles.sql), architecture, or setting up Docker, I’m happy to dive in further!

