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
    
    # This ensures routes are registered within the app's context
    with app.app_context():
        app.register_blueprint(job_routes)
        db.create_all() # Ensure tables exist on server startup

    return app

# This 'app' variable is what Vercel will look for and run
app = create_app()

# This part is for running it locally
if __name__ == '__main__':
    app.run(debug=True, port=5000)