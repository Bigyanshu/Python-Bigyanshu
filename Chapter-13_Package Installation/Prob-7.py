from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_World():
    return "<p> Hello Mahy </p>"
app.run()