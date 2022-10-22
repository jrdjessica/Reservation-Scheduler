"""CRUD operations."""

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
