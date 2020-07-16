
class ConverterRegistry():
    converters = {}

    @staticmethod
    def register(converter, lang_code):
        ConverterRegistry.converters[lang_code] = converter

    @staticmethod
    def get_converter(lang_code):
        return ConverterRegistry.converters[lang_code]
    
    """
    Returns supported languages in the converter as a list of strings
    """
    @staticmethod
    def get_language_codes():
        return list(ConverterRegistry.converters.keys())

    """
    Returns a list of objects where key is language code and value is
    pretty language name
    """
    @staticmethod
    def get_pretty_names():
        pretty_names_list = []
        for lang_code in ConverterRegistry.converters.keys():
            converter = ConverterRegistry.get_converter(lang_code)
            pretty_names_list.append({lang_code: converter.pretty_name})

        return pretty_names_list



