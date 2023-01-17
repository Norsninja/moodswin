from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId


# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Get the database and collection
db = client['MoodSwinger']
questions_collection = db['ms_survey_questions']
results_collection = db['ms_survey_results']

# Create the Flask app
app = Flask(__name__)
CORS(app, support_credentials=True)

# Route to handle requests for the questions
@app.route('/questions', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_questions():
    # Retrieve all documents
    documents = questions_collection.find({})

    # Convert the ObjectId objects to strings
    questions = [{key: str(value) if key == '_id' else value for key, value in doc.items()} for doc in documents]

    # Create a response with the appropriate CORS headers
    return jsonify(questions)

# Route to handle the submission of the survey form
@app.route('/submit', methods=['POST'])
@cross_origin(supports_credentials=True)
def submit_survey():
    # Get the form data from the request
    data = request.form

    # Convert the form data to a dictionary
    answers = {}
    for key, value in data.items():
        # Check if the value is a list (e.g. the "yesno" question)
        if isinstance(value, list):
            # If it's a list, store the first element
            answers[key] = value[0]
        else:
            answers[key] = value

    # Insert the answers into the ms_survey_results collection
    results_collection.insert_one(answers)

    # Convert the ObjectId to a string
    answers['_id'] = str(answers['_id'])

    # Create a response with the appropriate CORS headers
    return jsonify(answers)




# Run the app
if __name__ == '__main__':
    app.run(debug=True)
