from flask import Flask, render_template, request, url_for
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

# Provide Vite context processors and static assets directory
app.register_blueprint(assets_blueprint)

app.register_blueprint(vt_blueprint)

@app.get("/")
def index():
  return render_template("index.html")
