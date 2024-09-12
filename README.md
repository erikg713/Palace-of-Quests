# Palace of Quests

Palace of Quests is a Web3 quest-type application built for the Pi Network community. The app integrates the Pi Network SDK for peer-to-peer payments and runs on the Pi Network blockchain. Users can complete quests and make transactions using Pi tokens, while ensuring high levels of security and scalability.

## Project Structure

/palace-of-quests │ ├── backend (Flask) │ ├── app.py │ ├── requirements.txt │ ├── Dockerfile │ ├── routes │ ├── services │ ├── models │ └── utils │ ├── frontend (React) │ ├── public │ ├── src │ ├── package.json │ └── Dockerfile │ └── docker-compose.yml


## Features

- **Quest Completion**: Users can complete quests on the platform.
- **Pi Network Integration**: Pi tokens are used for payments and transactions through the Pi Network SDK.
- **Web3 Transactions**: The app supports Web3-based transactions that can interact with all blockchains.
- **Security**: The backend implements encryption, secure headers, and proper input validation to prevent data breaches and unauthorized access.

## Technologies Used

- **Frontend**: React, Axios
- **Backend**: Flask, Flask-SQLAlchemy, Gunicorn, Pi SDK
- **Database**: PostgreSQL
- **Containerization**: Docker and Docker Compose

## Installation

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/)

### Cloning the Repository

https://github.com/erikg713/palace-of-quests.git
