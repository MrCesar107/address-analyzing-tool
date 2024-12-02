from flask import Blueprint, request
import vt

vt_blueprint = Blueprint("vt", __name__, url_prefix="/vt")

client = vt.Client("")

@vt_blueprint.route("/analize_address", methods=["POST"])
def analize_address():
  address = request.form['address']
  return f"Formulario recibido Address: {address}"
