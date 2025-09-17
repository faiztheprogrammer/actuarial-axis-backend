from flask import Flask
from flask_cors import CORS
from config import DATABASE_URI
from db import db
from models.job import Job # This import ensures the model is known to SQLAlchemy
from routes.job_routes import job_routes

def create_app():
    """
    Application Factory Pattern: This is the standard for creating a 
    configurable and testable Flask application.
    """
    app = Flask(__name__)
    CORS(app) # Enable Cross-Origin Resource Sharing for the whole app

    # Configure the database connection from config.py
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app
    db.init_app(app)
    
    # Use app_context to ensure the application is configured before
    # registering blueprints and creating database tables.
    with app.app_context():
        # Register the blueprint and apply the '/api' prefix to all its routes.
        app.register_blueprint(job_routes, url_prefix='/api')
        
        # This will create the 'job' table in your Supabase database if it doesn't exist.
        db.create_all()

    return app

# This 'app' variable is what Vercel's serverless environment will look for.
app = create_app()

# This block is only for local development. It won't run on Vercel.
if __name__ == '__main__':
    app.run(debug=True, port=5000)