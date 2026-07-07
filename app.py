import os
from flask import Flask, jsonify
from database import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "Hello from URL Shortener!",
        "environment": {
            "DB_HOST": os.getenv("DB_HOST"),
            "DB_PORT": os.getenv("DB_PORT"),
        }
    }


@app.route("/users")
def users():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        )
    """)

    cursor.execute("""
        INSERT INTO users(name)
        VALUES ('Vinay')
    """)

    conn.commit()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )