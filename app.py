from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)
app.secret_key = "todocloud"

# Display the login page
@app.route("/")
def login():
    return render_template("login.html")

# Display the main dashboard after the user signs in
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Start the Flask development server
if __name__ == "__main__":
    app.run(debug=True)