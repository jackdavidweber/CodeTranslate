import json
import os
import subprocess

try:
    with open("../private_keys/firebase-access-key.json") as json_file:
        data = json.load(json_file)
        env = {
            **os.environ,
            "GOOGLE_APPLICATION_CREDENTIALS": json.dumps(data),
        }
        subprocess.Popen('/bin/bash', env=env).wait()
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json.dumps(data)
        
except:
    error_message = "Error creating environmental var. Make sure you have service key downloaded"
    error_message += "to private_keys/firebase-access-key.json. See readme for more instructions"
    print(error_message)

