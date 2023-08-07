from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "we def started this hackathon on time"

app.run(debug=True)