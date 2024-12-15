from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    adding_task = request.args.get("adding_task")
    print(adding_task)
    return render_template("ToDoList.html", adding_task=adding_task)