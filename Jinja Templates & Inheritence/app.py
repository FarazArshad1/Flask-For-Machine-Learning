from flask import Flask, redirect , url_for, render_template
import time
from employee import employee_data


app  = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title = 'Home Page')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/evaluate/<int:num>')
def evaluate(num):
    return render_template('evaluate.html',title = 'Evaluate', number = num)


@app.route('/employees')
def employee():
    return render_template('employees.html',title = "Employees", emp = employee_data)

@app.route('/employees/managers')
def managers():
    return render_template('manager.html',title = 'Managers' , emp = employee_data)




if __name__ == "__main__":
    app.run(debug=True)