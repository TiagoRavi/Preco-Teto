from flask import Blueprint

bp = Blueprint("main", __name__)


@bp.route("/api/status")
def status():
    return {"mensagem": "Healthy"}

