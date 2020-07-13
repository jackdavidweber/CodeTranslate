
class ConverterRegistry():
    converters = {}

    @staticmethod
    def register(converter, language):
        converters[language] = converter

    @staticmethod
    def get_converter(language):
        return converters[language]

