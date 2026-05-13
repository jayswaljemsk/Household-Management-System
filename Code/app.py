import os
import sys
import tempfile
from flask import Flask

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from backend.models import db, User

instance_dir = os.path.join(tempfile.gettempdir(), 'instance')
os.makedirs(instance_dir, exist_ok=True)

app = Flask(__name__, instance_path=instance_dir)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/household_services.db'
db.init_app(app)

with app.app_context():
    db.create_all()
    admin = User.query.filter_by(role='admin').first()
    if not admin:
        admin = User(email='admin@gmail.com', password='123', role='admin', user_status='active')
        db.session.add(admin)
        db.session.commit()

from backend.controllers import *

if __name__ == '__main__':
    app.run()
