from flask import Flask
from flask_cors import CORS
from .routes.prediction_routes import prediction_bp
from loguru import logger
import os

def create_app():
    app = Flask(__name__)
    
    CORS(app)
    
    log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'backend.log')
    logger.add(log_path, rotation="10 MB", retention="10 days", level="INFO", compression="zip")
    logger.info("Backend API Initializing...")
    # Register your prediction routes
    app.register_blueprint(prediction_bp, url_prefix='/api/v1')
    
    @app.route('/health', methods=['GET'])
    def health():
        return {"status": "healthy", "service": "crash-prediction-api"}, 200
        
    return app