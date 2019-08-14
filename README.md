# Falcon RESTful API boilerplate

It is sample RESTful API project using Falcon framework. 

## Project structure
* alembic - database migrations toolkit directory. All migrations are stored in alembic/versions folder.
* docs - documentation images and other stuff
* middlewares - falcon middlewares
* models - SQLAlchemy models
* resources - falcon resources
* schemas - marshmallow schemas
* utils - all other functions

## Features
* SQLAlchemy ORM - SQL toolkit
* Alembic - database migrations
* Marshmallow - object serialization/deserialization and requests validation

## Database schema
![alt text](docs/db_schema.png "DB schema")

## Endpoints
| Endpoint  	| Method  	| Request body  	| Description |
|---	|---	|---	|---	|
| /api/  	| GET  	| None  	| Returns status of an API   	|
| /api/groups  	| GET  	| None  	| Returns all groups  	|
|   	| POST  	| Fields by GroupSchema  	| Creates new group  	|
| /api/groups/{id}  	| GET  	| None  	| Returns single group  	|
|   	| PATCH  	| Partial fields by GroupSchema  	| Updates group data  	|
|   	| DELETE  	| None  	| Deletes group  	|
| /api/items  	| GET  	| None  	| Returns all items  	|
|   	| POST  	| Fields by ItemSchema  	| Creates new item  	|
| /api/items/{id}  	| GET  	| None  	| Returns single item  	|
|   	| PATCH  	| Partial fields by ItemSchema  	| Updates item data  	|
|   	| DELETE  	| None  	| Deletes item  	|
| /api/group/{group_id}/items  	| GET  	| None  	| Returns single group all items  	|
| /api/group/{group_id}/items/{item_id}  	| POST  	| None  	| Assigns item to a group  	|
|    	| DELETE  	| None  	| Deletes item from a group  	|

## Install and run
* Clone repo `git clone git@github.com:tomasrasymas/falcon-restful-api-boilerplate.git`
* Install libraries `pip install -r requirements.txt`
* Create database
    * Create alembic migration file `alembic revision --autogenerate -m "Groups and items"`. It will generate file into alembic/versions
    * Write changes to database `alembic upgrade head`
    * After that `sample.db` will be created in your root project directory
* Execute `app.py`. It uses `wsgiref` sample server to expose API on 8080 port
