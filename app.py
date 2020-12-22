from flask import Flask, render_template, jsonify, request
#POSTGRESS DEPENDENCY
from flask_sqlalchemy import SQLAlchemy

from os import environ

from flask_pymongo import PyMongo

import json

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'sqlite:///notepad.sqlite')

# db = SQLAlchemy(app)

# class Task(db.Model):
#     id = db.Column(db.integer, primary_key=True)
#     description = db.Column(db.String)


app.config['MONGO_URI'] = environ.get('MONGODB_URI', 'mongodb://localhost:27071/heroku-notepad')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html', name="James")
# POSTGRES
# @app.route('/api/tasks-postgres')
# def getTasksPostgres():
#     tasks = db.session.query(Task)
#     data = []

#     for task in tasks:
#         item = {
#             'id': task.id,
#             'description': task.description
#         }
#         data.append(item)
    
#     return jsonify(data)

@app.route('/api/tasks-mongo')
def getTasksMongo():
    tasks = mongo.db.tasks.find()
    data = []
    
    for task in tasks:
        item = {
            '_id': str(task['_id']),
            'description': task['description']
        }
        data.append(item)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)