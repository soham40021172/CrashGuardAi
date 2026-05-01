import joblib
import os
from crash_report.modeling.train import main
from crash_report.config import MODELS_DIR


def test_training_script():

    # Run training
    main()

    # Check model file
    model_path = MODELS_DIR / "crash_model.pkl"
    threshold_path = MODELS_DIR / "threshold.pkl"
    schema_path = MODELS_DIR / "feature_schema.pkl"

    assert model_path.exists(), "❌ Model not saved"
    assert threshold_path.exists(), "❌ Threshold not saved"
    assert schema_path.exists(), "❌ Schema not saved"

    # Load model
    model = joblib.load(model_path)

    # Basic check
    assert hasattr(model, "predict"), "❌ Model missing predict method"
    assert hasattr(model, "predict_proba"), "❌ Model missing predict_proba"

    print("✅ Training script test passed")