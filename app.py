from flask import Flask, jsonify
from db import get_all_todos

app = Flask(__name__)

@app.route("/")
def home(): 
    return "Welcome"
    

@app.route("/todos")
def todos():
    rows = get_all_todos()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
