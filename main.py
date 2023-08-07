from flask import Flask, request, jsonify #Flask is for the API
import psycopg2 #For using PostgreSQL
import urllib.parse as up #For PostreSQL
import os #For using .env
from dotenv import load_dotenv #For using .env


app = Flask(__name__) #Creating a Flask object
load_dotenv() #Loading the info from the .env file

########################################
up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DB_URL"])
db_connection = psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
cursor = db_connection.cursor()
########################################


@app.route("/")
def hello():
    return 200 #Returning 200 is considered to be a HTTP response and in this case 200 means the connection is OK.

@app.route('/addquote', methods=['POST'])
def receive_data():
    data = request.get_json()  # Assuming data is sent as JSON
    # Process the received data
    # You can perform any desired logic here
    return jsonify({"message": "Data received successfully"})

app.run(debug=True)