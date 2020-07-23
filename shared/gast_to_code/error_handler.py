class ErrorHandler():

    def __init__(self):
        self.error_number = 0
        self.error_obj = {}

    def unsupported_feature(self):
        error_name = "E" + str(self.error_number)
        self.error_number += 1

        error = {"errorType": "unsupportedFeature", "errorMessage": "Feature not supported"}
        self.error_obj[error_name] = error

        return "$$" + str(error_name) + "$$"

    def get_error_obj(self):
        return self.error_obj

    def __str__(self):
        return str(self.error_number)