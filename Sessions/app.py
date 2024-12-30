from flask import Flask, request, session, redirect, url_for, render_template_string

app = Flask(__name__)
app.secret_key = 'Bad_Secret_Key'

BASE_ROUTE = '/test'

@app.route(BASE_ROUTE + '/set_email', methods = ['GET','POST'])
def set_email():
    if request.method == 'POST':
        # Save the form data to session object
        session['email'] = request.form['email_address']
        return redirect(url_for('get_email'))

    return """
    <form method="post">
            <label for="email">Enter your email address:</label>
            <input type="email" id="email" name="email_address" required />
            <button type="submit">Submit</button
        </form>
    """

@app.route(BASE_ROUTE + '/get_email', methods = ["GET"])
def get_email():
    return render_template_string("""
            {% if session['email'] %}
                <h1>Welcome {{ session['email'] }}!</h1>
            {% else %}
                <h1>Welcome! Please enter your email <a href="{{ url_for('set_email') }}">here.</a></h1>
            {% endif %}
        """)

@app.route(BASE_ROUTE + '/delete_email')
def delete_email():
    # Clear the email stored in session object
    session.pop('email', default = None)
    return '<h1>Session deleted!</h1>'


if __name__ == "__main__":
    app.run()
