from flask import Blueprint, jsonify, current_app

company_bp = Blueprint("company", __name__)

@company_bp.route("/", methods=["GET"])
def get_companies():
    supabase = current_app.supabase
    result = supabase.table("companies").select("*").execute()
    return jsonify(result.data), 200