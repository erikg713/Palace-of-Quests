import os
import psycopg
from psycopg_pool import ConnectionPool

# --- Configuration ---
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "palace_of_quests_")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Palaceofquests")

pool = ConnectionPool(
    conninfo=f"host={DB_HOST} port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}",
    min_size=1,
    max_size=5,
    timeout=10,
)

def init_db():
    """Create payments table if it doesn't exist."""
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS payments (
                    payment_id VARCHAR(64) PRIMARY KEY,
                    data JSONB NOT NULL,
                    txid VARCHAR(128)
                );
            """)
        conn.commit()

def store_payment(payment_id: str, data: dict):
    """Insert or update a payment record."""
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO payments (payment_id, data)
                VALUES (%s, %s)
                ON CONFLICT (payment_id) DO UPDATE SET data = EXCLUDED.data
                """,
                (payment_id, psycopg.types.Jsonb(data))
            )
        conn.commit()

def update_payment(payment_id: str, txid: str):
    """Update the txid for a payment record."""
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE payments SET txid = %s WHERE payment_id = %s",
                (txid, payment_id)
            )
        conn.commit()

def get_payment(payment_id: str):
    """Fetch a payment record by ID."""
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT data, txid FROM payments WHERE payment_id = %s",
                (payment_id,)
            )
            row = cur.fetchone()
            if not row:
                return None
            data, txid = row
            result = dict(data)
            if txid:
                result['txid'] = txid
            return result

# --- Run table creation on import for dev convenience ---
init_db()
payments = {}

