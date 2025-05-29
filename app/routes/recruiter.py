from flask import Blueprint, jsonify, current_app

recruiter_bp = Blueprint("recruiter", __name__)

@recruiter_bp.route("/", methods=["GET"])
def get_recruiters():
    supabase = current_app.supabase
    result = supabase.table("recruiters").select("*").execute()
    return jsonify(result.data), 200