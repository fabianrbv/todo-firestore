from firebase_config import db

doc = {
    "message": "Connection successful!"
}

db.collection("test").add(doc)

print("Connected to Firestore successfully!")