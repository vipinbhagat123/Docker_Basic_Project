from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Backend via Nginx 🚀"

@app.route("/db")
def db_check():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db = cursor.fetchone()
    cursor.close()
    conn.close()
    return f"Connected to database: {db[0]} ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
