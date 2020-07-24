class ErrorHandler():

    def __init__(self):
        self.error_number = 0
        self.error_obj = {}

    def __add_error(self, error_type, error_message, other={}):
        """
        Adds error name and error key-value pair to error_obj.
        Returns the error name used surrounded by "$$".
        Requires error type and error message.
        Optionally, other can be passed in as a dictionary that can
        be used for fields other than error type and error message.
        """
        error_name = "E" + str(self.error_number)
        self.error_number += 1

        error = {
            "errorType": error_type,
            "errorMessage": error_message
        }
        error.update(other)

        self.error_obj[error_name] = error
        return "$$" + str(error_name) + "$$"


    def unsupported_feature(self):
        return self.__add_error("unsupportedFeature", "Feature not supported")

    def compilation(self):
        return self.__add_error("compilation", "input code does not compile")


    def impossible_translation(self):
        return self.__add_error("impossibleTranslation", "direct translation does not exist to this language")


    def invalid_arguments(self):
        return self.__add_error("invalidArguments", "arguments not valid")

    def unknown_error(self, filepath=None, artifact=None):
        error_message = "This error is unexpected. If encountered please file issue with description at https://github.com/jackdavidweber/cjs_capstone/issues"
        additional_error_info = {            
            "filePath": filepath,
            "artifact": artifact
        }
        return self.__add_error("unknown", error_message, additional_error_info)

    def get_error_obj(self):
        return self.error_obj

    def __str__(self):
        return str(self.error_obj)
