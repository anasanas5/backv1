from flask import Blueprint, request, jsonify, current_app

offer_bp = Blueprint("offer", __name__)

# 🔹 1. Toutes les offres (jobs)
@offer_bp.route("/", methods=["GET"])
def get_all_offers():
    try:
        supabase = current_app.supabase
        result = supabase.table("jobs").select("*").execute()
        return jsonify({"offers": result.data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🔹 2. Offres par recruteur (via recruiter_id → companies → jobs)
@offer_bp.route("/by-recruiter", methods=["GET"])
def get_offers_by_recruiter():
    recruiter_id = request.args.get("recruiter_id")
    if not recruiter_id:
        return jsonify({"error": "recruiter_id is required"}), 400

    try:
        supabase = current_app.supabase

        # Étape 1: trouver les entreprises de ce recruteur
        companies = supabase.table("companies").select("id").eq("recruiter_id", recruiter_id).execute()
        if not companies.data:
            return jsonify({"offers": []}), 200

        company_ids = [company["id"] for company in companies.data]

        # Étape 2: trouver les jobs associés à ces entreprises
        jobs = supabase.table("jobs").select("*").in_("company_id", company_ids).execute()
        return jsonify({"offers": jobs.data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
