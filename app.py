from flask import Flask, jsonify
from flask_cors import CORS
from db import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SQLALCHEMY_ENGINE_OPTIONS

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = SQLALCHEMY_ENGINE_OPTIONS or {}

    CORS(app)
    db.init_app(app)

    # register routes after db is initialised
    from routes.job_routes import job_routes
    app.register_blueprint(job_routes, url_prefix="/api")

    @app.route("/api/health")
    def health():
        return jsonify({"status": "ok"})

    return app

app = create_app()

@app.route("/api/ping", methods=["GET"])
def ping():
    """Lightweight keep-alive route for uptime monitoring."""
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(debug=True)
