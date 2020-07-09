import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os


def store_query(input_code, output_code, input_lang, output_lang):
    # Use a service account
    try:
        cred_object = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
    except:
        print("Please set GOOGLE_APPLICATION_CREDENTIALS environmental variable. See readme for more info")
        return
    
    cred = credentials.Certificate(cred_object)
    firebase_admin.initialize_app(cred)

    # only store code written on live heroku
    if "SHOULD_WRITE_TO_DATABASE" not in os.environ:
        return


    successful_translate = True
    if "Feature not supported" in output_code:
        successful_translate = False
    if "Error: did not compile" in output_code:
        successful_translate = False

    # Add user query and result to database
    db = firestore.client()
    doc_ref = db.collection(u'user-query').document()
    doc_ref.set({
        u'input_code': input_code,
        u'output_code': output_code,
        u'input_lang': input_lang,
        u'output_lang': output_lang,
        u'successful_translate': successful_translate
    })