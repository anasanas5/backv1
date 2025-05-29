from flask import Blueprint, jsonify, current_app

application_bp = Blueprint("application", __name__)

@application_bp.route("/", methods=["GET"])
def get_applications():
    supabase = current_app.supabase
    result = supabase.table("applications").select("*").execute()
    return jsonify(result.data), 200