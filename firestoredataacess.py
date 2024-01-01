import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Fetch the service account key JSON file from your Firebase project
cred = credentials.Certificate("parking-5ec09-firebase-adminsdk-8g17d-9e43a8aaa0.json")

# Initialize the Firebase app with the service account credentials
firebase_admin.initialize_app(cred)

# Access a Firestore database instance
db = firestore.client()

# Fetch a single document by ID
doc_ref = db.collection("names").document("RCbBBre4l6Clg7KHNNIZ")
doc = doc_ref.get()



# Fetch all documents in a collection
docs = db.collection('names').get()
print(doc.to_dict())
dic1=doc.to_dict()
print(doc.id)
for key, value in dic1.items():
    print(value)
    lis=[value]
    
print(lis)

# Query documents based on a condition
'''query = db.collection('collection_name').where('field', '==', 'value')
docs = query.get()
for doc in docs:
    print(f"Document ID: {doc.id}")
    print(f"Document data: {doc.to_dict()}")'''
