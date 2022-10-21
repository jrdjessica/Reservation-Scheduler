from flask import Flask
from model import connect_to_db

app = Flask(__name__)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
