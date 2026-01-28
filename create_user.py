from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    user = User(
        username='admin',
        password=generate_password_hash('admin123'),
        role='admin'
    )
    db.session.add(user)
    db.session.commit()
    print("Admin user created!")
