from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Get the database and collection
db = client['MoodSwinger']
collection = db['ms_survey_questions']

# Retrieve all documents
documents = collection.find({})

for doc in documents:
    print(doc)

# Remember to close the client connection
client.close()
