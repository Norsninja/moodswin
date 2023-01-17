from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId
import datetime
from cleaning_and_manipulating_data import clean_data
from visualizations import generate_visualization
import plotly.graph_objects as go

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Get the database and collection
db = client['MoodSwinger']
questions_collection = db['ms_survey_questions']
results_collection = db['ms_survey_results']

# Create the Flask app
app = Flask(__name__)


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

    # Construct the document to be inserted
    doc = {key: int(value) if key != '_id' and key != 'Pick a Color' and value.isdigit() else value for key, value in data.items()}


    doc['_id'] = ObjectId()
    doc['date_submitted'] = datetime.datetime.now()

    # Insert the document into the ms_survey_results collection
    results_collection.insert_one(doc)

    # Convert the ObjectId to a string
    doc['_id'] = str(doc['_id'])

    # Create a response with the appropriate CORS headers
    return jsonify(doc)

# Route to handle requests for the most recent survey results
@app.route('/results', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_most_recent_results():
    # Print out the query used to retrieve the document
    print('Retrieving document with query: {}'.format(results_collection.find().sort([('date_submitted', -1)]).limit(1)))
    
    # Get the ObjectId of the most recent survey result
    most_recent_result = results_collection.find().sort([('date_submitted', -1)]).limit(1)[0]
    result_id = most_recent_result['_id']

    # Retrieve the document with the given ObjectId
    result = results_collection.find_one({'_id': result_id})

    # Convert the ObjectId to a string
    result['_id'] = str(result['_id'])

    # Create a response with the appropriate CORS headers
    return jsonify(result)
    
@app.route('/results/all', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_all_results():
    results = results_collection.find({})
    results = [{key: str(value) if key == '_id' else value for key, value in doc.items()} for doc in results]
 #   df = clean_data(results)

    
    return jsonify(results)


# Route to handle requests for the visualization
# @app.route('/visualization', methods=['GET'])
# @cross_origin(supports_credentials=True)
# def get_visualization():
    # Retrieve all documents from the collection
    results = list(results_collection.find())

    # Clean and manipulate the data
    df = clean_data(results)
    
    print(df.columns)
    print(df.dtypes)

    # Generate the visualization
    fig = generate_visualization(df)
    generate_visualization(df)

    # Convert the figure object into a JSON object
    json_fig = fig.to_json()

    # Create a response with the appropriate CORS headers
    return jsonify(json_fig)

# Run the app 
if __name__ == '__main__':
    app.run(host='192.168.0.17', port=5000)
