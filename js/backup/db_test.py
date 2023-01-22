from pymongo import MongoClient
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import traceback

app = Flask(__name__)
CORS(app, support_credentials=True)  # enable CORS for the app

def fetch_questions_from_database():
    try:
        # Connect to the MongoDB server
        client = MongoClient('mongodb://localhost:27017/')

        # Get the database and collection
        db = client['MoodSwinger']
        collection = db['ms_survey_questions']

        # Retrieve all documents
        documents = collection.find({})

        # Extract the list of questions from the documents
        questions = [doc['question'] for doc in documents]

        # Remember to close the client connection
        client.close()
    
    except Exception as e:  # catch any exceptions that may occur
        print(f'An error occurred: {e}')  # log the error message
        return None  # return None to indicate that an error occurred
    
    return questions
     


@app.route('/questions', methods=['GET'])
@cross_origin(origin='http://127.0.0.1:5000/', supports_credentials=True)
def serve_questions_page():
    questions = fetch_questions_from_database()  # retrieve the list of questions from the database
    print(questions)  # Debugging statement
    # Convert the ObjectId objects to strings
    questions = [{key: str(value) if key == '_id' else value for key, value in doc.items()} for doc in questions]
    
    # Set the Access-Control-Allow-Origin header to allow cross-origin requests from the client
    response = jsonify(questions)
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000'  # allow requests from any origin
    return response
    
@app.route('/results', methods=['POST'])
def save_results():
    # Get the form data
    data = request.form

    # Connect to the MongoDB server
    client = MongoClient('mongodb://localhost:27017/')

    # Get the database and collection
    db = client['MoodSwinger']
    collection = db['ms_survey_results']

    # Insert the data into the collection
    collection.insert_one(data)

    # Remember to close the client connection
    client.close()



# Run the app
if __name__ == '__main__':
    app.run()