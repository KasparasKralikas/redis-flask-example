# Redis + Flask Example

Simple example showcasing possibility to cache API responses with [Redis](https://redis.io/) using python [Flask](https://flask.palletsprojects.com/) application as a server.

Flask app fetches [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) to retrieve todos.

### How to Launch
1. Make sure you have [Docker](https://docs.docker.com/get-docker/) installed.
2. Then run the following:
```
docker-compose up
```

### Endpoints

Flask app by default starts on localhost port 5000 and has the following endpoints for retrieving todos:
- **GET: localhost:5000/get_todos** - returns all the todos in a JSON format;
- **GET: localhost:5000/get_todos/_id_** - returns the todo with a specified **_id_** in a JSON format.

### Caching benefits

Caching is used to store the results of requests that require expensive operations. So the next time the same request can be served much faster. A popular choice for such a task as showcased in this example is Redis in-memory cache that can store key-value pairs. Cache often serves as an intermittent layer between the application serving the request and the entity that provides the requested resource. When the request is received that requires a particular resource, the application checks the cache first for the said resource. If the resource exists in the cache, it is simply returned. If the cache doesn't contain the requested resource, that resource is retrieved the expensive way from the database or some sort of service or/and is computed by the application. Then the resource is stored in the cache for a set amount of time.

In this particular example retrieving all of the todos initially takes from **_120 ms_** up to **_700 ms_** depending on the load of the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/). Once the data is cached, the same retrieval of all of the todos can be performed in about **_15 ms_** - at least a tenfold efficiency improvement. The same can be seen when retrieving individual todos by their **_id_**. Initially, it takes anywhere from **_120 ms_** up to **_400 ms_** to retrieve the individual todo. Once the todo is cached any subsequent request can be performed in about **_15 ms_**.
