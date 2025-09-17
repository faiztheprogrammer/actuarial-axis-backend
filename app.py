from flask import Flask
from flask_cors import CORS
from config import DATABASE_URI
from db import db
from models.job import Job
from routes.job_routes import job_routes

# This is a standard Flask app initialization
app = Flask(__name__)
CORS(app)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and register blueprints
db.init_app(app)
app.register_blueprint(job_routes)

@app.route('/api/test', methods=['GET'])
def test_route():
    return {"message": "Flask backend is running!"}

# The if __name__ == '__main__': block is not needed for Vercel
# but doesn't hurt, and is good for local development.
if __name__ == '__main__':
    app.run(debug=True, port=5000)