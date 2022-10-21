"""Data model for users and appointments."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """"Users."""

    __tablename__ = 'users'

    username = db.Column(db.String(25), primary_key=True)

    appointment = db.relationship('Appointment', back_populates='user')

    def __repr__(self):
        return f'<User username={self.username}'


class Appointment(db.Model):
    """User appointments."""

    __tablename__ = 'appointments'

    date = db.Column(db.DateTime, primary_key=True)
    username = db.Column(db.String(25), db.ForeignKey(
        'users.username'), nullable=False)

    user = db.relationship('Appointment', back_populates='appointment')

    def __repr__(self):
        return f'<Appointment date={self.date} username={self.username}'
