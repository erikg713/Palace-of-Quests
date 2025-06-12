```markdown
# Palace of Quests Backend

This is the backend service for Palace of Quests, a Web3 application
integrating the Pi Network SDK to enable secure transactions and user authentication. Built with Flask and PostgreSQL, it supports seamless integration with the frontend.

---

## Features

- **RESTful API**: Endpoints for smooth interaction with the frontend.
- **JWT Authentication**: Secure user sessions and data access.
- **Pi Network Integration**: Handle Pi coin transactions securely.
- **PostgreSQL Support**: Robust and scalable database solution.
- **Dockerized Deployment**: Simplifies setup and scaling.

---

## Prerequisites

Before setting up the backend, ensure you have:

- **Python**: v3.9+ installed.
- **PostgreSQL**: Running database instance.
- **Docker**: Optional but recommended for containerized deployment.
- **Pi Network App Credentials**: Obtain from the Pi Developer Portal.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/erikg713/Palace-of-Quests.git
   cd Palace-of-Quests/backend
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**: Create a `.env` file in the root directory with these keys:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_random_secret_key
   DATABASE_URL=postgresql://user:password@localhost:5432/palace_of_quests
   PI_APP_ID=your_pi_app_id
   PI_API_KEY=your_pi_api_key
   ```

5. **Initialize the Database**:
   ```bash
   flask db upgrade
   ```

---

## Development

1. **Run the Development Server**:
   ```bash
   flask run
   ```

   The server will start at [http://localhost:5000](http://localhost:5000).

2. **Test API Endpoints**:
   Use tools like Postman or cURL to interact with the API.

---

## API Endpoints

### Authentication
- `POST /auth/register`: Register a new user.
- `POST /auth/login`: Authenticate and return a JWT.

### Payments
- `POST /payment/initiate`: Start a Pi coin transaction.
- `POST /payment/complete`: Confirm a transaction.

### Quests
- `GET /quests`: Retrieve all quests.
- `POST /quests`: Add a new quest.

---

## Docker Deployment

1. **Build the Docker Image**:
```markdown
    ```bash
   docker build -t palace-of-quests-backend .
   ```

3. **Run the Container**:
   ```bash
   docker run -p 5000:5000 --env-file .env palace-of-quests-backend
   ```

4. **Using Docker-Compose**:
   ```bash
   docker-compose up
   ```

---

## Deployment

The backend can be deployed on platforms like:
- AWS EC2 or Lightsail
- Heroku
- Google Cloud
- DigitalOcean

Ensure environment variables on the hosting platform match your `.env` file.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```

3. Commit your changes and push to the branch.
4. Open a pull request.

---

## License

This project is licensed under the PIOS License.
```

---
