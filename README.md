# TODOIST
This is a small full stack project built so as to learn how to make API calls with JavaScript.

## Built with 
* HTML
* CSS
* JavaScript
* Python Flask 
* SQLite Database

## The Backend
The backend consists of a REST API built using Flask, resources are stored using SQLite

### The API


| ROUTE | METHOD | DESCRIPTION |
|-------|---------|-------------|
| /todos | GET     | return all todos |
| /todo/ID | GET    | return a todo with ID |
| /todos   | POST    | creates a todo resource |
| /todo/ID | PATCH    | update a todo resource |
| /todo/ID | PUT     | replace a todo resource |
| /todo/ID  | DELETE | delete a todo resource |


# The Front-end
This is an HTML CSS and JavaScript frontend using `fetch` for api calls