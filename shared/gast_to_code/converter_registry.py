
class ConverterRegistry():
    converters = {}

    @staticmethod
    def register(converter, lang_code):
        ConverterRegistry.converters[lang_code] = converter

    @staticmethod
    def get_converter(lang_code):
        return ConverterRegistry.converters[lang_code]
    
    """
    Returns supported language codes in the converter as a list of strings
    """
    @staticmethod
    def get_language_codes():
        return list(ConverterRegistry.converters.keys())

    """
    Returns a dictionary where keys are language codes and values are
    pretty language names
    """
    @staticmethod
    def get_pretty_names():
        pretty_names_dict = {}
        for lang_code in ConverterRegistry.converters.keys():
            converter = ConverterRegistry.get_converter(lang_code)
            pretty_names_dict[lang_code] = converter.pretty_name

        return pretty_names_dict



