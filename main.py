from flask import Flask #Flask is for the API
import psycopg2 #For using PostgreSQL

app = Flask(__name__)

@app.route("/")
def hello():
    return 200 #Returning 200 is considered to be a HTTP response and in this case 200 means the connection is OK.

app.run(debug=True)

