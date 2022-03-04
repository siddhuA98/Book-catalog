from app import create_app, db  # app/__init__ (ROOT PACKAGE)
from app.auth.models import User


flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
flask_app.run()
