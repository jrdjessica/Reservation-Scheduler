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
