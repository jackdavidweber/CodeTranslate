import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os

# Initialize app
try:
    cred_object = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
except:
    print("Please set GOOGLE_APPLICATION_CREDENTIALS environmental variable. See readme for more info")
    

cred = credentials.Certificate(cred_object)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://codetranslate-feedback.firebaseio.com'
})

db = firestore.client()
#docs = db.collection(u'user-query').stream()
docs = db.collection(u'user-query').where(u'timestamp', u'>=', '2020-07-28T16:50:49.305244+00:00').stream()

count = 0
for doc in docs:
    count += 1
    print(f'{doc.to_dict()}')

print(count)
#2178 user-queries since demo 
#10309 total user-queries