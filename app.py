import redis
import requests
import json
from flask import Flask, jsonify

EXPIRATION_TIME_IN_SECS = 20

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


# Getters

def _get_todos(_id=None):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    return response.json()


def _get_todo(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
    return response.json()


# Caching

def get_from_cache(key, getter):
    value = cache.get(key)
    if value is None:
        retrieved_value = getter(key)
        cache.setex(key, EXPIRATION_TIME_IN_SECS, json.dumps(retrieved_value))
        return retrieved_value
    else:
        return json.loads(value)


# Routes

@app.route('/todos')
def get_todos():
    data = get_from_cache('todos', _get_todos)
    return jsonify(data)


@app.route('/todos/<id>')
def get_todo(id):
    data = get_from_cache(id, _get_todo)
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5000)
