from flask import Flask, request, jsonify #Flask is for the API
from flask_cors import CORS  # Import the CORS module, its for some web security thing, we might be able to remove this later
import psycopg2 #For using PostgreSQL
import urllib.parse as up #For PostreSQL
import os #For using .env
from dotenv import load_dotenv #For using .env


app = Flask(__name__) #Creating a Flask object
CORS(app)
load_dotenv() #Loading the info from the .env file
up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DB_URL"])

@app.route("/")
def hello():
    return 200 #Returning 200 is considered to be a HTTP response and in this case 200 means the connection is OK.

@app.route('/addquote', methods=['POST'])
def receive_data():
    data = request.get_json()  # Assuming data is sent as JSON
    insert_query = """
        INSERT INTO quotes (quote_text, page_number, work_title, author_title, keywords)
        VALUES (%s, %s, %s, %s, %s)
    """

    quote_data = (
        data["quote_text"],
        data["page"],
        data["work_title"],
        data["author"],
        data["keywords"].replace(" ", "").split(",")
    )
    db_connection = psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
    cursor = db_connection.cursor()

    cursor.execute(insert_query, quote_data)

    db_connection.commit()
    cursor.close()
    db_connection.close()

    return jsonify({"message": "Data received successfully"})

app.run(debug=True)