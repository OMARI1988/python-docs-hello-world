from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello dede! JoJo has a very big head :)"
