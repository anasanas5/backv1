from flask import Blueprint, jsonify, current_app

notification_bp = Blueprint("notification", __name__)

@notification_bp.route("/", methods=["GET"])
def get_notifications():
    supabase = current_app.supabase
    result = supabase.table("notifications").select("*").execute()
    return jsonify(result.data), 200