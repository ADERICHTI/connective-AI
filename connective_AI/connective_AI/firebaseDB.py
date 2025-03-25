import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

from dotenv import load_dotenv
import os
import json

load_dotenv()
key = json.loads(os.getenv('GOOGLE_CLOUD_CREDENTIALS'))
# print(key)

# Use the service account file to authenticate
firebase_config = key
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

def updateDB(new_data, collection_id="commands", document_id="command001"):
    doc_ref = db.collection(u''+collection_id).document(document_id)
    doc_ref.update(new_data)

def readDB(collection_id="commands", document_id="command001"):
    doc_ref = db.collection(u'commands')
    docs = doc_ref.stream()
    for doc in docs:
        if doc.id == document_id:
            return doc.to_dict()

print(readDB())

# updateDB({
#     u"command": "play music /@ book",
#     u"id": "RICHY-16384",
#     u"passkey": "richy'sAI",
#     u"time_tag": str(datetime.now())})