from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    viewer = User(
        username='viewer',
        password=generate_password_hash('viewer123'),
        role='viewer'
    )
    db.session.add(viewer)
    db.session.commit()
    print("Viewer user created!")
