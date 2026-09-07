from flask import Flask, request

app = Flask(__name__)

secret_key = "super_secret_123"

@app.route("/calculate")
def calculate():
    expression = request.args.get("expression")
    return str(eval(expression))
