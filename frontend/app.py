from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


# Default route
@app.route('/')
def loginpage():
    return render_template('loginpage.html')


# User login
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    response = requests.post('http://backend:5001/login', json={
        'email': email,
        'password': password
    })

    if response.status_code == 200:
        username = response.json()['username']
        return redirect(url_for('homepage', username=username))
    return render_template('loginpage.html', message='Invalid credentials')


# Homepage route
@app.route('/homepage')
def homepage():
    username = request.args.get('username')
    return render_template('homepage.html', username=username)


# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']

        response = requests.post('http://backend:5001/register', json={
            'username': username,
            'email': email,
            'password': password,
            'gender': gender
        })

        if response.status_code == 201:
            return render_template('loginpage.html', message='User registered successfully!')

        # Update the error message handling to include the specific email
        error_message = response.json().get('message', 'An error occurred.')
        return render_template('register.html', message=error_message)

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
