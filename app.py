from flask import Flask, escape, request
import random

app = Flask(__name__)

students = {}
classes = {}
#classes = 
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/students', methods = ['POST'])
def create_student():
    print(request)
    id = random.randint(1,10000)
    content = request.json
    students[id] = content["name"]
    return {
        "id" : id,
        "name" : content["name"]
    }, 201

@app.route('/students/<id>', methods = ['GET'])
def retreive_student(id):
    if int(id) in students:
        return {
            "id" : id,
            "name" : students[int(id)]
        } 
    else:
        return "Student ID not found"

@app.route('/classes', methods = ['POST'])
def add_class():
    id = random.randint(10000,20000)
    content = request.json
    content["id"] = id
    content["students"] = []
    classes[id] = content
    return content

@app.route('/classes/<id>', methods = ['GET'])
def retreive_classes(id):
    if int(id) in classes:
        return classes[int(id)]
    else:
        return "Class ID not found"

@app.route('/classes/<id>', methods = ['POST'])
def add_student_to_class(id):
    content = request.json
    if int(id) in classes:
        if int(content["student_id"]) in students:
            std_id = int(content["student_id"])
            std_name = students[std_id]
            updated_class = classes[int(id)]
            updated_class["students"] = [{
                "id" : std_id,
                "name" : std_name
            }]
        
        return updated_class
    else:
        return "Class ID not found"

