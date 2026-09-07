from flask import Flask, request
import sqlite3

app = Flask(__name__)

password = "admin123"
api_key = "sk_test_123456789"

@app.route("/user")
def user():
    user_id = request.args.get("id")

    query = "SELECT * FROM users WHERE id=" + user_id

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(query)

    result = eval(user_id)

    return str(result)
