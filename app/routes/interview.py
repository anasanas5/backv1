from flask import Blueprint, jsonify, current_app

interview_bp = Blueprint("interview", __name__)

@interview_bp.route("/", methods=["GET"])
def get_interviews():
    supabase = current_app.supabase
    result = supabase.table("interviews").select("*").execute()
    return jsonify(result.data), 200