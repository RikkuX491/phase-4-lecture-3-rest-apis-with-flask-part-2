# Phase 4, Lecture 3: Rest APIs with Flask (Part 2)

## Lecture Topics

- Handling PATCH and DELETE requests
- Rest APIs with Flask (PATCH and DELETE requests)

## Key Vocab

- Representational State Transfer (REST): a convention for developing applications that use HTTP in a consistent, human-readable, machine-readable way.
- Application Programming Interface (API): a software application that allows two or more software applications to communicate with one another.
- PATCH: an HTTP request method that signifies that the client is attempting to update a resource with new information.
- DELETE: an HTTP request method that signifies that the client is attempting to delete a resource.

## Introduction

In today's lecture, we will add functionality to our REST API to handle PATCH and DELETE requests.

## Setup

1. Fork and then Clone this repository.

2. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then run `pipenv install` in your terminal to install the required libraries.

3. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

4. Enter the command `cd server` in the terminal to move into the server directory.

5. Run these commands in the terminal (make sure that you are in the `server` directory before running these terminal commands):

```py
export FLASK_APP=app.py

export FLASK_RUN_PORT=7000
```

6. We will write code in the `app.py` file to build functionality to handle PATCH and DELETE requests to the `/hotels/<int:id>` route such that it follows the convention for REST APIs.

7. Enter the command `flask run` or `python app.py` in the terminal to run the Flask app (make sure that you are in the `server` directory before running these terminal commands).

- Note: You can enter the command `flask run --debug` which is another option to run the flask app with debug mode on.

8. We will use Postman to test our app's functionality for handling PATCH and DELETE requests.