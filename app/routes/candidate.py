from flask import Blueprint, jsonify, current_app

candidate_bp = Blueprint("candidate", __name__)

@candidate_bp.route("/", methods=["GET"])
def get_candidates():
    supabase = current_app.supabase
    result = supabase.table("candidates").select("*").execute()
    return jsonify(result.data), 200