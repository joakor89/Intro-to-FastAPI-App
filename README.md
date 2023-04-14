# Building A Movie App with Fastapi

FastAPI It is a modern, high-performance framework for building APIs with Python

Characteristics
a. Fast
b. Less errors
c. Easy and intuitive
d. Robust
e. Based on standards

FastAPI used framework:
1. Starlette: Asynchronous framework for building services and is one of the fastest in Python.
2. Pydantic: Responsible for data validation.
3. Uvicorn

# What the API will be about

The project will be an API that will provide related information about movies, so we will have the following:

```sh
1. Movies Consultancy: To achieve this we will use the GET method and request all the data of our movies

2. Movie Filtering: It will also request information about movies by their id and by the category to which they belong, for this we will use the GET method and we will help ourselves with the route parameters and the query parameters.

3. Movie Registering: Using the POST method to register the data of our movies and we will also use the pydantic library schemes to manage the data.

4. Modifying and Deleting: Finally, to complete our CRUD, we will modify and delete data in our application, for which we will use the PUT and DELETE methods respectively.
```


# HTTP Protocol
The HTTP protocol is one that defines a set of request methods that indicate the action to be performed for a specific server resource.

1. POST – Create a new resource.
2. PUT: Modify an existing resource.
3. GET: consult information about a resource.
4. DELETE: delete a resource.


# Installing, creating  & setting up FastAPI App

# Virtual Environment
```sh
1. creating virtual environment: py -m venv venv
2. source venv/bin/activate
3. pip install fastapi
4. pip install uvicorn
```

# App Setting Up
```sh
1. from fastapi import FastAPI
2. app = FastAPI()
3. def message():
    return "Hello there!"
```

# Running App 
# Running at Terminal

```sh
A. Default Port
uvicorn main:app --reload --port 5000
B. Same Net
uvicorn main:app --reload --port 5000 --host 0.0.0.0
```

```sh
A. To see the results from other devices, you must put your IP 
address followed by the port, that is: x.x.x.x:5000

B. On Linux, you can see your IP address with
the hostname -I command. The IP is the first address shown.
```

# 
