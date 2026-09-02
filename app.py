from flask import Flask, jsonify
from db import get_all_todos

app = Flask(__name__)

@app.route("/")
def home(): 
    return "Welcome"
    

if __name__ == "__main__":
    app.run(debug=True)
