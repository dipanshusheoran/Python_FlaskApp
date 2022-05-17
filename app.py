from datetime import datetime
import imp
from turtle import title
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    created_date = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} {self.title}"

@app.route("/")
def hello():
    todo = Todo(title='Learn Python', desc='Step one to be a Data Engineer.')
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template("home.html",allTodo = allTodo)

@app.route("/about")
def about():
    allTodo = Todo.query.all()
    print(allTodo)
    return "About this page"

if __name__ == "__main__":
    app.run(debug=True,port=8000)