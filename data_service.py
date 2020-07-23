import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os
from datetime import datetime, timezone


class DataService:
    instance = None

    def __init__(self):
        self.running_locally = True
        # Use a service account
        try:
            cred_object = json.loads(
                os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
        except:
            print(
                "Please set GOOGLE_APPLICATION_CREDENTIALS environmental variable. See readme for more info"
            )
            return

        cred = credentials.Certificate(cred_object)
        firebase_admin.initialize_app(cred)

        # only store code written on live heroku
        if "SHOULD_WRITE_TO_DATABASE" in os.environ:
            self.running_locally = False

        self.db = firestore.client()

    @staticmethod
    def getInstance():
        if DataService.instance:
            return DataService.instance
        else:
            DataService.instance = DataService()
            return DataService.instance

    def store_query(self, input_code, output_code, input_lang, output_lang,
                    session_id):
        if self.running_locally:
            return

        if "Feature not supported" in output_code:
            doc_ref = self.db.collection(u'feature-not-supported').document()
            doc_ref.set({
                u'input_code': input_code,
                u'output_code': output_code,
                u'input_lang': input_lang,
                u'output_lang': output_lang,
                u'timestamp': datetime.now(timezone.utc).isoformat(),
                u'session_id': session_id
            })
        elif "Error: did not compile" in output_code:
            doc_ref = self.db.collection(u'did-not-compile').document()
            doc_ref.set({
                u'input_code': input_code,
                u'output_code': output_code,
                u'input_lang': input_lang,
                u'output_lang': output_lang,
                u'timestamp': datetime.now(timezone.utc).isoformat(),
                u'session_id': session_id
            })
        else:
            doc_ref = self.db.collection(u'user-query').document()
            doc_ref.set({
                u'input_code': input_code,
                u'output_code': output_code,
                u'input_lang': input_lang,
                u'output_lang': output_lang,
                u'timestamp': datetime.now(timezone.utc).isoformat(),
                u'session_id': session_id
            })
