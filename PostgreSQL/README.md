Database README (PostgreSQL)

Overview

The PostgreSQL database for PiQuest stores data for users, items, quests, and marketplace transactions. It is optimized with indexes for fast access to frequently queried data, and relational structures ensure consistency and scalability.

Database Structure

The database is composed of key tables, each representing an essential part of the game’s data.

Tables

1. User Table - Stores information about each user in the game.


2. Inventory Table - Stores items in the marketplace and user-owned assets.


3. Quest Table - Manages quest details and links them to user progress.


4. Transaction Table - Logs purchases and bridges to other networks.



Database Schema

Below is a schema representation of the PostgreSQL database tables.

Users
------------------------
id             SERIAL PRIMARY KEY
username       VARCHAR(50) UNIQUE NOT NULL
password_hash  VARCHAR(128) NOT NULL
wallet_address VARCHAR(100) NOT NULL

Inventory
------------------------
id             SERIAL PRIMARY KEY
item_name      VARCHAR(100)
item_type      VARCHAR(50)
price          NUMERIC(10, 2)
user_id        INTEGER REFERENCES Users(id)

Quests
------------------------
id             SERIAL PRIMARY KEY
name           VARCHAR(100) NOT NULL
is_completed   BOOLEAN DEFAULT FALSE
user_id        INTEGER REFERENCES Users(id)

Transactions
------------------------
id             SERIAL PRIMARY KEY
user_id        INTEGER REFERENCES Users(id)
item_id        INTEGER REFERENCES Inventory(id)
transaction_type VARCHAR(20)
amount         NUMERIC(10, 2)
date           TIMESTAMP DEFAULT CURRENT_TIMESTAMP

Database Setup and Migration

1. Setup PostgreSQL Database:

Create a new PostgreSQL database (e.g., piquest_db).

Update the DATABASE_URL in your backend .env file with the connection string.



2. Run Migrations: If using Flask-Migrate, you can handle migrations with the following commands:

flask db init          # Initialize migrations folder
flask db migrate       # Generate initial migration
flask db upgrade       # Apply the migration to the database



Explanation of Key Tables

Users: Contains user-specific data like username, password_hash, and wallet_address for Pi Network transactions.

Inventory: Holds item details, prices, and user ownership information.

Quests: Stores quest details and completion status, linking each quest to a specific user.

Transactions: Logs transactions and asset bridges to Ethereum, aiding in user history and cross-chain interaction.

