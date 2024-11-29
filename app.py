from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "db",
    "user": "root",
    "password": "example",
    "database": "testdb"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
