from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS  # Import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Enable CORS for all routes
    CORS(app)

    from app import routes  # Import routes after initializing app

    return app