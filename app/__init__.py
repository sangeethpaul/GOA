from flask import Flask
from flask_cors import CORS
import os



def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow all origins (for development)
    # OR for production:
    CORS(app, resources={r"/api/*": {"origins": "https://your-frontend-url.onrender.com"}})

    # Configuration
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), '../knowledge')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app