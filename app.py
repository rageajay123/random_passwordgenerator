from flask import Flask, render_template, request, jsonify
import random
import string
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    filename = data.get('filename')
    length = 12
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))

    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (filename, password) VALUES (?, ?)", (filename, password))
    conn.commit()
    conn.close()

    return jsonify({'password': password})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
