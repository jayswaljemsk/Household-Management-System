from flask import Flask
from backend.models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///household_services.db'
db.init_app(app)

with app.app_context():
    db.create_all()
    admin = User.query.filter_by(role='admin').first()
    if not admin:
        admin = User(email='admin@gmail.com', password='123',role='admin',user_status='active')
        db.session.add(admin)
        db.session.commit()

from backend.controllers import *

if __name__ == '__main__':
    app.run()
