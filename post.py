from pymongo import MongoClient
from flask import Flask, request

app = Flask(__name__)

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Get the database and collection
db = client['MoodSwinger']
collection = db['my_survey_results']

@app.route('/results', methods=['POST'])
def add_to_database():
    # Retrieve the JSON object from the request
    data = request.get_json()

    # Insert the data into the collection
    collection.insert_one(data)

    # Return a success message
    return 'Successfully added data to the database'

if __name__ == '__main__':
    app.run()
