import os
import logging
from flask import Flask, render_template, send_from_directory
from src.webgui import GUI, close_application

# Set up logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Create Flask app
app = Flask(__name__)

# Base path for directories
base_path = os.path.dirname(__file__)

# Routes
@app.route("/")
def root():
    return render_template("index.html")

@app.route("/navbar")
def navbar():
    return render_template("navbar.html")

@app.route("/home")
def home():
    return render_template("login.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/forms")
def forms():
    return render_template("forms.html")

@app.route("/table")
def table():
    return render_template("table.html")

@app.route("/jumbotron")
def jumbotron():
    return render_template("jumbotron.html")

@app.route("/public/<path:filename>")
def serve_public_file(filename):
    return send_from_directory(os.path.join(base_path, "public"), filename)

@app.route("/close")
def close_server():
    close_application()

if __name__ == "__main__":
    try:
        logging.info("Starting GUI with Flask app...")
        GUI(
            app=app,
            server="flask",
            port=3000,
            width=1024,
            height=600,
        ).run()
    except Exception as e:
        logging.error("Error starting application: %s", e)