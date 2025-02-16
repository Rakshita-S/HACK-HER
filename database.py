from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost_and_found.db'  # Use SQLite for simplicity
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables (if they don't exist yet)