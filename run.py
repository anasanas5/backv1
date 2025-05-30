from flask_cors import CORS
from app import create_app

app = create_app()

# Ajout du middleware CORS pour accepter les requêtes du frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
