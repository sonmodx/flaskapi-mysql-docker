# flaskapi-mysql-docker

This project was created to practice my docker CLI skills as part of SDPX course. Learning how to create database with mysql by docker container for running mysql server and volume for persisting data. Furthermore I tried using Flask(micro framework written in Python) to make CRUD API.

## Requirements

- Docker
- Flask(Python)
- mysql-connector-python

## Notice

- Running localhost on port 8081 connect to `db-dev` database's name
- Running localhost on port 8082 connect to `db-test` database's name
  -- See more information in docker-compose.yaml file.

## API Reference

#### Get all users

```http
  GET /getUsers
```

#### Get user by ID

```http
  GET /getUser/<uid>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uid`     | `string` | **Required**. ID of user to fetch |

#### Create user by name and age

```http
  POST /createUser/<name>/<age>
```

| Parameter | Type     | Description                         |
| :-------- | :------- | :---------------------------------- |
| `name`    | `string` | **Required**. name of user to fetch |
| `age`     | `string` | **Required**. age of user to fetch  |

#### Delete user by ID

```http
  DELETE /deleteUser/<uid>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uid`     | `string` | **Required**. ID of user to fetch |

#### Update user by ID, name and age

```http
  PATCH /updateUser/<uid>/<name>/<age>
```

| Parameter | Type     | Description                         |
| :-------- | :------- | :---------------------------------- |
| `uid`     | `string` | **Required**. ID of user to fetch   |
| `name`    | `string` | **Required**. name of user to fetch |
| `age`     | `string` | **Required**. age of user to fetch  |

## Run Locally

Clone the project

```bash
  git clone https://github.com/sonmodx/flaskapi-mysql-docker.git
```

Go to the project directory

```bash
  cd flaskapi-mysql-docker
```

Run docker container using docker-compose

```bash
  docker compose up [OPTIONS]
```

Stop and remove containers for service defined in compose file

```bash
  docker compose down
```
