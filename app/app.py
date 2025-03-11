from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection settings from environment variables
DB_HOST = os.getenv("POSTGRES_HOST", "postgres-service")
DB_NAME = os.getenv("POSTGRES_DB", "mydatabase")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")

def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

@app.route("/")
def home():
    return jsonify({"message": "Flask app is running!"})

@app.route("/db")
def test_db():
    conn = connect_db()
    if conn:
        return jsonify({"message": "Connected to PostgreSQL successfully!"})
    else:
        return jsonify({"error": "Database connection failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)