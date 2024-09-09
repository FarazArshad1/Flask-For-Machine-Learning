from flask import Flask

# create app
app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>welcome to the home page</h1>'

@app.route("/welcome/steve")
def welcome_steve():
    return '<h1>Welcome Steve'

@app.route('/welcome/<user>')
def welcome_tony(user): 
    return f'<h1>Welcome {user.title()}</h1>'

if __name__ == "__main__":
    app.run(debug=True)