import os
import logging
from pymongo import MongoClient
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.cors = CORS(self.app, support_credentials=True)  # enable CORS for the app
        self.db_url = os.environ.get("MONGO_URL")  # get the database URL from the environment
        self.client = MongoClient(self.db_url)  # create a connection pool
        self.logger = logging.getLogger(__name__)  # create a logger

    def fetch_questions_from_database(self):
        try:
            # Get the database and collection
            db = self.client['MoodSwinger']
            collection = db['ms_survey_questions']

            # Retrieve all documents
            documents = collection.find({})

            # Extract the list of questions from the documents
            questions = [doc['question'] for doc in documents]
        
        except Exception as e:  # catch any exceptions that may occur
            self.logger.error(f'An error occurred: {e}')  # log the error message
            return None  # return None to indicate that an error occurred
        
        return questions
    
    ## route establishing /results 
    @self.app.route('/questions', methods=['GET'])
    @cross_origin(origin='http://127.0.0.1:5000/', supports_credentials=True)
    def serve_questions_page(self):
        questions = self.fetch_questions_from_database()  # retrieve the list of questions from the database
        self.logger.debug(questions)  # Debugging statement
        # Convert the ObjectId objects to strings
        questions = [{key: str(value) if key == '_id' else value for key, value in doc.items()} for doc in questions]
        
        # Set the Access-Control-Allow-Origin header to allow cross-origin requests from the client
        response = jsonify(questions)
        response.headers['Access-Control-Allow-Origin'] = '*'  # allow requests from any origin
        return response
        
    @self.app.route('/survey', methods=['GET'])
    @cross_origin(origin='http://127.0.0.1:5000/', supports_credentials=True)
    def serve_survey_page(self):
        questions = self.fetch_questions_from_database()  # retrieve the list of questions from the database
        self.logger.debug(questions)  # Debugging statement
        # Convert the ObjectId objects to strings
        questions = [{key: str(value) if key == '_id' else value for key, value in doc.items()} for doc in questions]
        
        # Set the Access-Control-Allow-Origin header to allow cross-origin requests from the client
        response = render_template('survey.html', questions=questions)
        response.headers['Access-Control-Allow-Origin'] = '*'  # allow requests from any origin
        return response
        
    @self.app.route('/results', methods=['POST'])
    @cross_origin(origin='http://127.0.0.1:5000/', supports_credentials=True)
    def save_results(self):
        # Get the form data
        data = request.form
        self.validate_data(data)  # Validate the data before saving it

        # Get the database and collection
        db = self.client['MoodSwinger']
        collection = db['ms_survey_results']

        # Insert the data into the collection
        collection.insert_one(data)

    def validate_data(self, data):
        # Validate the data being sent to the database
        # Add custom validations here

        @self.app.route('/visualization', methods=['GET'])
        @cross_origin(origin='http://127.0.0.1:5000/', supports_credentials=True)
        def serve_visualization_page(self):
            # Get the data from the database
            db = self.client['MoodSwinger']
            collection = db['ms_survey_results']
            data = collection.find({})

            # Generate the data visualizations
            # Add code to generate the data visualizations here

            # Set the Access-Control-Allow-Origin header to allow cross-origin requests from the client
            response = render_template('visualization.html', data=data)
            response.headers['Access-Control-Allow-Origin'] = '*'  # allow requests from any origin
            return response

    def run(self):
        # Run the app
        self.app.run()

if __name__ == '__main__':
    app = App()
    app.run()