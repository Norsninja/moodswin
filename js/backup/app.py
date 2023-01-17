from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Get the database and collection
db = client['MoodSwinger']
collection = db['ms_survey_questions']

# Create the Flask app
app = Flask(__name__)
CORS(app, support_credentials=True)

# Route to handle requests for the questions
@app.route('/questions', methods=['GET'])
def get_questions():
    # Retrieve all documents
    documents = collection.find({})

    # Convert the ObjectId objects to strings
    questions = [{key: str(value) if key == '_id' else value for key, value in doc.items()} for doc in documents]

    # Create a response with the appropriate CORS headers
    response = flask.jsonify(questions)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response



# Run the app
if __name__ == '__main__':
    app.run()
