from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://josephpeterjece2021:AJ9Hg6xTtQBUCoGr@cluster1.xaacunv.mongodb.net/?retryWrites=true&w=majority')

# Accessing the database
db = client['Python']

# Accessing the collection
collection = db['python']

# Text to be inserted
text_to_insert = {
    "content": "This is some example text to be inserted into MongoDB."
}

# Inserting the document into the collection
inserted_doc = collection.insert_one(text_to_insert)

# Output the ObjectID of the inserted document
print("Document inserted with ObjectID:", inserted_doc.inserted_id)
