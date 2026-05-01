import sys
import os

# 🔥 Fix import issue
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)