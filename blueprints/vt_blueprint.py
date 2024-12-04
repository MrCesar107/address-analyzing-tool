from flask import Blueprint, request, jsonify
import requests
import vt
import os

vt_blueprint = Blueprint("vt", __name__, url_prefix="/vt")

@vt_blueprint.route("/analize_address", methods=["POST"])
def analize_address():
  address = request.form.get("address")
  analysis = analize_url(address)
  return analysis

@vt_blueprint.route("/get_url_analysis/<analysis_id>", methods=["GET"])
def get_url_analysis(analysis_id):
  url = f"{build_endpoint("analyses")}/{analysis_id}"
  headers = {
    "accept": "application/json",
    "x-apikey": os.getenv("VT_API_KEY")
  }
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    result = response.json()
    return jsonify(result)
  else:
    return f"Hubo un error al obtener los resultados: {response.text}", response.status_code


def analize_url(url):
  if not url:
    return jsonify({"error": "No se proporcionó una URL"}), 400

  endpoint = build_endpoint("urls")
  headers = {
    "accept": "application/json",
    "x-apikey": os.getenv("VT_API_KEY"),
    "content-type": "application/x-www-form-urlencoded"
  }
  data = { "url": url }
  response = requests.post(endpoint, headers=headers, data=data)

  if response.status_code == 200:
    result = response.json()
    analysis_id = result["data"]["id"]
    return jsonify({"message": "URL enviada para análisis", "analysis_id": analysis_id})
  else:
    return jsonify({"error": "Error al enviar la URL", "details": response.text}), response.status_code


def build_endpoint(path):
  return f"{os.getenv("VT_URL_ENDPOINT")}/{path}"