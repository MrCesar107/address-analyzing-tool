from flask import Blueprint, request
import vt
import os

vt_blueprint = Blueprint("vt", __name__, url_prefix="/vt")

client = vt.Client(os.getenv('VT_API_KEY'))

@vt_blueprint.route("/analize_address", methods=["POST"])
def analize_address():
  address = request.form['address']
  return f"Formulario recibido Address: {address}"
