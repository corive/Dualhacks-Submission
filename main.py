from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "we def started this hackathon on time"

@app.route("/hyein")
def i_think_you_can_name_this_function_anything():
    return "mul juseyo!"

app.run(debug=True)