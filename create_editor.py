from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    user = User(
        username='editor',
        password=generate_password_hash('editor123'),
        role='editor'
    )
    db.session.add(user)
    db.session.commit()
    print("Editor user created!")
