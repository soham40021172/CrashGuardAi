from flask import Blueprint, request, jsonify
from ..services.model_service import ModelService
from loguru import logger

prediction_bp = Blueprint('prediction', __name__)
model_service = ModelService()

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    logger.info("New request received for SHAP prediction.")
    
    try:
        # The service now returns the full dictionary with SHAP explanations
        result = model_service.predict_severity(data)
        return jsonify({
            "status": "success",
            "data": result
        }), 200
    except Exception as e:
        logger.error(f"Prediction Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500