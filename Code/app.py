from flask import Flask
from Code.backend.models import db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/household_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

print("App is setup")

# import AFTER app creation
import Code.backend.controllers


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()