import json
import os


try:
    with open("../private_keys/firebase-access-key.json") as json_file:
        data = json.load(json_file)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json.dumps(data)
except:
    error_message = "Error creating environmental var. Make sure you have service key downloaded"
    error_message += "to private_keys/firebase-access-key.json. See readme for more instructions"
    print(error_message)

