from flask import Flask
from flask_cors import CORS
from config import DATABASE_URI
from db import db
from models.job import Job
from routes.job_routes import job_routes

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        app.register_blueprint(job_routes)
        # You might need to create tables if they don't exist
        # db.create_all() # Comment this out after the first successful run

    return app

# This 'app' variable is what Vercel's WSGI server will look for.
app = create_app()

# The if __name__ == '__main__' is for local development and won't be run on Vercel