/palace-of-quests
│
├── backend (Flask)
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── routes
│   │   └── quest_routes.py
│   ├── services
│   │   └── pi_payment_service.py
│   ├── models
│   │   └── user_model.py
│   └── utils
│       └── security.py
│
├── frontend (React)
│   ├── public
│   ├── src
│   │   ├── components
│   │   │   └── QuestComponent.js
│   │   ├── services
│   │   │   └── apiService.js
│   │   └── App.js
│   ├── package.json
│   └── Dockerfile
│
└── docker-compose.yml
# Palace-of-Quests
**Palace of Quests** is an innovative Web3 quest-based game built for the Pi Network community. Players embark on various quests and challenges, completing tasks to earn Pi tokens through peer-to-peer payments. The app integrates the Pi secure token transactions and provides a seamless experience for users on the Pi blockchain.
