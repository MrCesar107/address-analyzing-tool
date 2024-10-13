from flask import Flask, render_template
from assets_blueprint import assets_blueprint

app = Flask(
  __name__,
  static_url_path="/",
  static_folder="public",
  template_folder="templates"
)

# Provide Vite context processors and static assets directory
app.register_blueprint(assets_blueprint)

@app.get("/")
def index():
  return render_template("index.html")
