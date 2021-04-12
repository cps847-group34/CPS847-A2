from flask import Flask, render_template
from flask_session import Session
from config import Config

app=Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run()