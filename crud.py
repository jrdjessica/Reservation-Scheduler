"""CRUD operations."""

from datetime import datetime
from model import Appointment


def check_appointment(appointment):
    """Check if appointment exists."""

    if Appointment.query.filter(Appointment.date == appointment).first():
        return True
    return False


def add_reservation(username, appointment):
    """Add reservation."""

    reservation = Appointment(username=username, date=appointment)

    return reservation


def view_reservations(username):
    """View user's reservation(s)."""

    user_reservations = Appointment.query.filter(
        Appointment.username == username).all()

    return user_reservations


def check_same_day_appointment(username, appointment):
    """Check if user has a same day appointment (if so, return true)."""

    user_reservations = Appointment.query.filter(
        Appointment.username == username).all()

    # appointment = '2022-01-01T12:30'
    appointment = datetime.strptime(appointment, '%Y-%m-%dT%H:%M')

    for reservation in user_reservations:
        if reservation.date.year == appointment.year and reservation.date.month == appointment.month and reservation.date.day == appointment.day:
            return True
    return False
