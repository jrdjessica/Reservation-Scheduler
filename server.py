from flask import Flask, render_template
from model import connect_to_db

app = Flask(__name__)


@app.route('/')
def show_login():
    """User log in page."""

    return render_template('login.html')


@app.route('/search')
def search_appointments():
    """Search for appointments and view search results."""

    return render_template('search-apts.html')


@app.route('/view')
def get_scheduled_appointments():
    """View all the scheduled appointments for the current user."""

    return render_template('view-apts.html')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
