from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from assets_blueprint import assets_blueprint
from blueprints.vt_blueprint import vt_blueprint
import os

load_dotenv()

app = Flask(
  __name__,
  static_url_path="/",
  static_folder="public",
  template_folder="templates"
)

app.config['VT_API_KEY'] = os.getenv("VT_API_KEY")
app.config['VT_URL_ENDPOINT'] = os.getenv("VT_URL_ENDPOINT")

# Provide Vite context processors and static assets directory
app.register_blueprint(assets_blueprint)

app.register_blueprint(vt_blueprint)

@app.get("/")
def index():
  return render_template("index.html")

@app.get("/test")
def test():
  return jsonify({"key": os.getenv("VT_API_KEY")})
