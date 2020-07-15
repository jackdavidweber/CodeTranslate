
class ConverterRegistry():
    converters = {}

    @staticmethod
    def register(converter, language):
        ConverterRegistry.converters[language] = converter

    @staticmethod
    def get_converter(language):
        return ConverterRegistry.converters[language]
    
    """
    Returns supported languages in the converter as a list of strings
    """
    @staticmethod
    def get_languages():
        return list(ConverterRegistry.converters.keys())

