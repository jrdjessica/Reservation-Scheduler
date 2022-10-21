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
        return f'<User username={self.username}>'


class Appointment(db.Model):
    """User appointments."""

    __tablename__ = 'appointments'

    appointment_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), db.ForeignKey(
        'users.username'), nullable=False)
    date = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='appointment')

    def __repr__(self):
        return f'<Appointment date={self.date} username={self.username}>'


def example_data():
    user1 = User(username='user1')

    appointments = [
        Appointment(user=user1, date=datetime.strptime('2017-06-01T08:30',
                    '%Y-%m-%dT%H:%M')),
        Appointment(user=user1, date=datetime.strptime('2017-02-01T16:30',
                    "%Y-%m-%dT%H:%M"))
    ]

    db.session.add_all(appointments)
    db.session.commit()


def connect_to_db(flask_app, db_uri="postgresql:///apts", echo=True):
    """Connect the database to the Flask app."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)


if __name__ == "__main__":
    from server import app

    connect_to_db(app)

    # creates tables and sample data
    db.create_all()
    example_data()

    print("Connected to the db!")
