
class ConverterRegistry():
    converters = {}

    @staticmethod
    def register(converter, language):
        ConverterRegistry.converters[language] = converter

    @staticmethod
    def get_converter(language):
        return ConverterRegistry.converters[language]

