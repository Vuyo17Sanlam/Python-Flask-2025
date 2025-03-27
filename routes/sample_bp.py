from flask import Blueprint, request, render_template
from pprint import pprint


HTTP_NOT_FOUND = 404
sample_bp = Blueprint("sample_bp", __name__)


@sample_bp.get("/")
def sample_bp_page():
    return render_template(
        "sample_bp.html",
    )
