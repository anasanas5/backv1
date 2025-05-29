from flask import Flask
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Supabase configuration
    app.supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_KEY")
    )

    # Auth routes
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # ✅ Enregistrer toutes les autres routes
    from app.routes.recruiter import recruiter_bp
    from app.routes.candidate import candidate_bp
    from app.routes.company import company_bp
    from app.routes.offer import offer_bp
    from app.routes.application import application_bp
    from app.routes.interview import interview_bp
    from app.routes.notification import notification_bp

    app.register_blueprint(recruiter_bp, url_prefix="/recruiters")
    app.register_blueprint(candidate_bp, url_prefix="/candidates")
    app.register_blueprint(company_bp, url_prefix="/companies")
    app.register_blueprint(offer_bp, url_prefix="/offers")
    app.register_blueprint(application_bp, url_prefix="/applications")
    app.register_blueprint(interview_bp, url_prefix="/interviews")
    app.register_blueprint(notification_bp, url_prefix="/notifications")

    return app