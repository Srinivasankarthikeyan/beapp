from flask import Flask
from config import Config
from extensions import db, migrate, cors


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # Register blueprints
    from modules.health import health_bp
    from modules.users import users_bp
    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(users_bp, url_prefix="/api")

    return app


# For Gunicorn and local development
app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)