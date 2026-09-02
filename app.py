from flask import Flask, jsonify, request
from db import get_all_todos, add_todo()

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
