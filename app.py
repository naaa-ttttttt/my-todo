from flask import Flask, jsonify, request, render_template
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
    return jsonify({"message": "Todo created successfully"})

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo_route(todo_id):
    update_todo(todo_id)
    return jsonify({"message": "Todo status update"})


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo_route(todo_id):
    delete_todo(todo_id)
    return jsonify({"message": "Todo task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
