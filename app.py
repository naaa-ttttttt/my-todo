from flask import Flask, jsonify, request
from db import get_all_todos, add_todo, update_todo, delete_todo

app = Flask(__name__)

@app.route("/")
def home(): 
    return "Welcome"
    

@app.route("/todos")
def todos():
    rows = get_all_todos()
    return jsonify(rows)


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    task = data["task"]
    add_todo(task)
    return jsonify({"message: Todo added"})

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    update_todo(todo_id)
    return jsonify({"message": "Todo status update"})


if __name__ == "__main__":
    app.run(debug=True)
