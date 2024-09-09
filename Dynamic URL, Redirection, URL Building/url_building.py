from flask import Flask, redirect , url_for
import time


app  = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Welcome To Home</h1>'

@app.route('/passed/<sname>/<int:marks>')
def passed(sname,marks):
    return f"Congratz{sname} you've passed with {marks} marks"

@app.route('/failed/<sname>/<int:marks>')
def failed(sname,marks):
    return f"Sorry {sname}, you've failed with {marks}"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed",sname=name, marks=num))
    else:
        time.sleep(1)
        return redirect(url_for('passed', sname=name, marks=num))
        

if __name__ == '__main__':
    app.run(debug=True)

