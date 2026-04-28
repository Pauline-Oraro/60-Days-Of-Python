# APIs & HTTP Protocol

## What is an API?

**API** stands for **Application Programming Interface**. In the context of web development, an API is a set of defined rules and specifications that allow different software applications to communicate with each other.

Web APIs are the defined interfaces through which interactions happen between a service and applications that use it. They define:

- **What requests** can be made
- **How** to make those requests
- **What format** the data will be returned in (usually **JSON** or **XML**)

> **Important:** An API is like a waiter in a restaurant — you (the client) don't go into the kitchen (the server) yourself. You tell the waiter (the API) what you want, and the waiter brings it back to you. You never need to know how the kitchen works.

---

## Why Are APIs Important?

- Allow applications to share data and functionality without exposing internal logic
- Enable integration between different platforms and services
- Allow content created in one place to be dynamically posted and updated across multiple platforms
- Power social media integrations, payment systems, maps, weather data, and much more

**Real-world examples:**

- Twitter's REST API lets developers access tweets, trends, and user data
- Countries API provides data about countries (population, capital, currency, flag)
- Cat Breeds API provides information about different cat breeds
- Google Maps API lets developers embed maps and location data in their apps

---

## Types of Web APIs

| Type | Description | Status |
|------|-------------|--------|
| **REST** | Representational State Transfer — uses HTTP methods, lightweight, returns JSON | Most widely used today |
| **SOAP** | Simple Object Access Protocol — XML-based, strict rules | Older, being phased out |
| **GraphQL** | Query language for APIs — client specifies exactly what data it needs | Modern alternative to REST |

> **Important:** The web industry has been moving **away from SOAP** towards **REST** because REST is simpler, faster, and works naturally with HTTP.

---

## What is a RESTful API?

A **RESTful API** is an API that follows the principles of **REST (Representational State Transfer)**. It uses standard **HTTP request methods** to perform operations on data.

### REST Principles

- **Stateless** — each request contains all information needed; the server stores no session data
- **Client-Server** — the client and server are separate and communicate only through the API
- **Uniform Interface** — consistent, predictable URLs and methods
- **Resource-Based** — data is treated as resources, each with its own unique URL

---

## HTTP — Hypertext Transfer Protocol

**HTTP** is the communication protocol between a **client** (browser or app) and a **server** (where data lives).

- A browser is an **HTTP client** — it sends requests
- A web server is an **HTTP server** — it sends responses
- HTTP is used to deliver HTML files, images, JSON data, scripts, and more

### HTTP Request-Response Cycle

```
Client (Browser/App)                    Server
        |                                  |
        |  --- HTTP Request (GET /home) --> |
        |                                  |
        |  <-- HTTP Response (200 OK) ----- |
        |       + HTML/JSON data            |
        |                                  |

```

> **Important:** Every time you visit a webpage, your browser sends an HTTP request and the server sends back an HTTP response. This cycle completes millions of times per second across the internet.

---

## Structure of an HTTP Message

Both HTTP **requests** and **responses** share a similar structure:

```
1. Initial Line (Request Line or Status Line)
2. Header Fields (zero or more)
3. Blank Line (marks end of headers)
4. Optional Message Body
```

---

## HTTP Request

### Initial Request Line

Contains three parts separated by spaces:

```
METHOD  /path/to/resource  HTTP/version
GET     /                  HTTP/1.1
```

### Example Request Headers

```
GET / HTTP/1.1
Host: thirtydaysofpython-v1-final.herokuapp.com
Connection: keep-alive
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)
Accept: text/html,application/xhtml+xml,application/xml
Accept-Language: en-GB,en;q=0.9
```

| Header Field | Purpose |
|-------------|---------|
| `Host` | The domain name of the server |
| `Connection` | Whether to keep the connection alive after the request |
| `User-Agent` | Information about the browser/client making the request |
| `Accept` | The content types the client can handle |
| `Accept-Language` | The preferred language of the client |
| `Cache-Control` | Instructions for caching the request |

---

## HTTP Response

### Initial Response Line (Status Line)

Contains three parts:

```
HTTP/version  StatusCode  Reason
HTTP/1.1      200         OK
HTTP/1.1      404         Not Found
```

### HTTP Status Codes

| Code | Category | Meaning |
|------|----------|---------|
| `200` | ✅ Success | OK — request succeeded, resource returned |
| `201` | ✅ Success | Created — new resource successfully created |
| `204` | ✅ Success | No Content — request succeeded, nothing to return |
| `301` | 🔄 Redirect | Moved Permanently — resource has a new URL |
| `400` | ❌ Client Error | Bad Request — the request was malformed |
| `401` | ❌ Client Error | Unauthorized — authentication is required |
| `403` | ❌ Client Error | Forbidden — server refuses to fulfill the request |
| `404` | ❌ Client Error | Not Found — resource does not exist |
| `500` | 🔥 Server Error | Internal Server Error — something went wrong on the server |

> **Important:** Status codes in the **200s** mean success, **400s** mean the client made an error, and **500s** mean the server made an error.

---

## HTTP Message Body

An HTTP message may include a **body** — the actual data being sent or received.

| Context | Body Contains |
|---------|--------------|
| **Response body** | The requested resource (HTML page, JSON data, image, etc.) |
| **Request body** | User-submitted form data, uploaded files, JSON payload |

### Important Body Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Content-Type` | Describes the format of the body | `application/json`, `text/html` |
| `Content-Length` | The size of the body in bytes | `Content-Length: 348` |

### Common Content Types (MIME Types)

| MIME Type | Format |
|-----------|--------|
| `text/html` | HTML page |
| `application/json` | JSON data |
| `text/plain` | Plain text |
| `text/css` | CSS stylesheet |
| `image/gif` | GIF image |
| `image/png` | PNG image |
| `multipart/form-data` | File upload |

---

## HTTP Request Methods (CRUD)

RESTful APIs map HTTP methods to **CRUD operations** (Create, Read, Update, Delete).

| HTTP Method | CRUD Operation | Description |
|-------------|----------------|-------------|
| `GET` | **Read** | Retrieve data from the server. Should only fetch data — never modify it. |
| `POST` | **Create** | Send data to the server to create a new resource (e.g. new user, new post). |
| `PUT` | **Update** | Replace an existing resource entirely with new data. |
| `PATCH` | **Partial Update** | Update only specific fields of an existing resource. |
| `DELETE` | **Delete** | Remove a resource from the server. |

### Example API Endpoints

```
GET    /api/users          → Get all users
GET    /api/users/1        → Get user with ID 1
POST   /api/users          → Create a new user
PUT    /api/users/1        → Update user with ID 1 (full update)
PATCH  /api/users/1        → Update specific fields of user 1
DELETE /api/users/1        → Delete user with ID 1
```

> **Important:** `GET` requests should **never** modify data. Any operation that changes data should use `POST`, `PUT`, `PATCH`, or `DELETE`.

---

## Building a RESTful API with Flask

Flask is a lightweight Python web framework that makes it easy to build RESTful APIs.

### Basic Flask API Example

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Pauline", "country": "Kenya"},
    {"id": 2, "name": "Alex", "country": "Uganda"}
]

# GET — Read all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET — Read one user
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    return jsonify(user) if user else ('Not found', 404)

# POST — Create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

# DELETE — Delete a user
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [u for u in users if u['id'] != id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

---

## API Response Format (JSON)

Most modern APIs return data in **JSON (JavaScript Object Notation)** format.

```json
{
  "status": "success",
  "data": {
    "id": 1,
    "name": "Pauline Oraro",
    "country": "Kenya",
    "city": "Nairobi"
  }
}
```

> **Important:** JSON is the standard format for API data exchange because it is lightweight, human-readable, and supported natively by JavaScript and easily parseable by Python using the `json` module.

---

## Quick Reference

| Concept | Description |
|---------|-------------|
| **API** | Interface that allows two applications to talk to each other |
| **REST** | Architecture style using HTTP methods for CRUD operations |
| **HTTP** | Communication protocol between client and server |
| **GET** | Retrieve data |
| **POST** | Create data |
| **PUT** | Update/replace data |
| **DELETE** | Delete data |
| **200** | Request succeeded |
| **404** | Resource not found |
| **500** | Server error |
| **JSON** | Standard data format for API responses |
| **Endpoint** | A specific URL where an API can be accessed |
