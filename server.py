from flask import Flask, render_template, request, redirect, session, flash
from model import connect_to_db, db

import crud

app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def show_login():
    """User log in page."""

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def user_login():
    """User logs in."""

    username = request.form.get('username')
    session['username'] = username

    return redirect('/search')


@app.route('/search')
def search_appointments():
    """Search for appointments and view search results."""

    return render_template('search-apts.html')


@app.route('/check', methods=['POST'])
def check_appointment():
    """Check availability of appointment."""

    appointment = request.form.get('appointment')
    username = session.get('username')

    check = crud.check_appointment(appointment)

    if not check:
        reservation = crud.add_reservation(username, appointment)
        db.session.add(reservation)
        db.session.commit()
        flash('Success. Your reservation is saved.')
    else:
        flash('This reservation is taken. Choose a different time.')

    return redirect('/search')


@app.route('/view')
def get_scheduled_appointments():
    """View all the scheduled appointments for the current user."""

    return render_template('view-apts.html')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
