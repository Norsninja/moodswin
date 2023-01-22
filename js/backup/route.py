from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Get the database and collection
db = client['MoodSwinger']
collection = db['ms_survey_results']

# Create a document to post 
document = {'mental_confidence': 8, 'physical_confidence': 5, 'shame_vs_pride': 3, 'extroversion_vs_introversion': 7, 'appetite': 4, 'color': 'blue', 'pain': 2, 'exercise': True, 'sleep': 9} 
  
# Insert the document into the collection 
collection.insert_one(document) 

 # Retrieve all documents 
documents = collection.find({}) 

 # Print out each document 
for doc in documents: 
    print(doc)  

 # Remember to close the client connection 
client.close()