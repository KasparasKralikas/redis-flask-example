import redis
import requests
from flask import Flask, jsonify

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/todos')
def get_todos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    return jsonify(response.json())

@app.route('/todos/<id>')
def get_todo(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
    return jsonify(response.json())

app.run(port=5000)
