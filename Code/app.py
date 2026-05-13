from flask import Flask
from Code.backend.models import db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/household_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# IMPORTANT
import Code.backend.controllers

print("App is setup")


@app.route("/")
def test():
    return "App working"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(role='admin').first()

        if not admin:
            admin = User(
                email='admin@gmail.com',
                password='123',
                role='admin',
                user_status='active'
            )

            db.session.add(admin)
            db.session.commit()

    app.run()