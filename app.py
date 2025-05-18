from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Route to render signup form
@app.route('/')
def signup_form():
    return render_template('signup.html')

# Route to handle form submission
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Store data in SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

    return "Signup successful!"

@app.route('/view_users')
def view_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, email, password FROM users")  # Avoid showing passwords directly
    users = cursor.fetchall()
    conn.close()

    return render_template('view_users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)