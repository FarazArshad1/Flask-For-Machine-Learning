from flask import Flask, redirect , url_for
import time


app  = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Welcome To Home</h1>'

@app.route('/passed')
def passed():
    return "Congratz you've passed"

@app.route('/failed')
def failed():
    return "Sorry, you've failed"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
        return redirect(url_for('passed'))
        

if __name__ == '__main__':
    app.run(debug=True)

