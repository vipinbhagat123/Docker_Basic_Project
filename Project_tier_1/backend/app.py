from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def hello():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"Backend connected to database: {db_name[0]} ✅"
    except Exception as e:
        return f"Database connection failed ❌ : {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def hello():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"Backend connected to database: {db_name[0]} ✅"
    except Exception as e:
        return f"Database connection failed ❌ : {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
