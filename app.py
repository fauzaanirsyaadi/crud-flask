from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = 'super secret string'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Employee(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"Employee('{self.name}', '{self.username}', '{self.email}', '{self.password}')"


@app.route('/', methods=['GET', 'POST'])
def Index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':

        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        employee = Employee(name, username, email, password)
        db.session.add(employee)
        db.session.commit()
        flash('employee successfully added')
        return redirect(url_for('Index', employee=employee))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        data = Employee.query.get(request.form.get('id'))
        data.name = request.form['name']
        data.username = request.form['username']
        data.email = request.form['email']
        data.password = request.form['password']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index', data=data))


@app.route('/delete/<id>/', methods=['GET'])
def delete(id):
    if request.method == 'GET':
        data = Employee.query.get(id)

        db.session.delete(data)
        db.session.commit()
        flash("Employee Deleted Successfully")

        return redirect(url_for('Index', data=data))


if __name__ == '__main__':
    app.run(debug=True)
