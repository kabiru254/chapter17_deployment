from app import app, db
from app.models import User


# Add database models and instance to a flask shell session
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
