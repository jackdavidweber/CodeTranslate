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

    def compilation(self):
        error_name = "E" + str(self.error_number)
        self.error_number += 1

        error = {"errorType": "compilation", "errorMessage": "input code does not compile"}
        self.error_obj[error_name] = error

        return "$$" + str(error_name) + "$$"

    def impossible_translation(self):
        error_name = "E" + str(self.error_number)
        self.error_number += 1

        error = {"errorType": "impossibleTranslation", "errorMessage": "direct translation does not exist to this language"}
        self.error_obj[error_name] = error

        return "$$" + str(error_name) + "$$"

    def invalid_arguments(self):
        error_name = "E" + str(self.error_number)
        self.error_number += 1

        # TODO: make this more descriptive in next iteration
        error = {"errorType": "invalidArguments", "errorMessage": "arguments not valid"}
        self.error_obj[error_name] = error

        return "$$" + str(error_name) + "$$"
    
    def unknown_error(self, filepath=None, artifact=None):
        error_name = "E" + str(self.error_number)
        self.error_number += 1

        # TODO: make this more descriptive in next iteration
        error = {
            "errorType": "unknown",
            "errorMessage": "This error is unexpected. If encountered please file issue with description at https://github.com/jackdavidweber/cjs_capstone/issues",
            "filePath": filepath,
            "artifact": artifact
            }
        self.error_obj[error_name] = error

        return "$$" + str(error_name) + "$$"

    def get_error_obj(self):
        return self.error_obj

    def __str__(self):
        return str(self.error_obj)