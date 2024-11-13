"""
pip install flask
pip install flask_restful
pip install flask_sqlalchemy
pip install python-dotenv

create a requirements.txt by using  "pip freeze > requirements.txt"
create a .gitignore by using  "touch .gitignore"
for installing all dependency libs "pip install -r requirements.txt"
"""
from flask import Flask, request , jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/<random_string>")
def return_backwards_string(random_string):
    # comment
    return "".join(reversed(random_string))

@app.route("/get-mode")
def get_mode():
    return os.environ.get("MODE")

if __name__ == "__main__":
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=8080)