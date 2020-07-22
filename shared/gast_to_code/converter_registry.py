class ConverterRegistry():
    converters = {}

    @staticmethod
    def register(converter, lang_code):
        ConverterRegistry.converters[lang_code] = converter

    @staticmethod
    def get_converter(lang_code):
        return ConverterRegistry.converters[lang_code]

    """
    Returns supported language codes in the converter as a list of strings.
    Only returns language codes where is_beta is false
    """

    @staticmethod
    def get_fully_supported_language_codes():
        fully_supported_language_codes = []
        for lang_code in ConverterRegistry.converters.keys():
            converter = ConverterRegistry.get_converter(lang_code)

            if not converter.is_beta:
                fully_supported_language_codes.append(lang_code)

        return fully_supported_language_codes

    """
    Returns a dictionary where keys are language codes are dicts
    with pretty names, and booleans indicating information about whether 
    the language is in beta, supports input and supports output
    """

    @staticmethod
    def get_lang_dict():
        lang_dict = {}
        for lang_code in ConverterRegistry.converters.keys():
            converter = ConverterRegistry.get_converter(lang_code)

            lang_specific_dict = {
                "name": converter.name,
                "is_beta": converter.is_beta,
                "is_input_lang": converter.is_input_lang,
                "is_output_lang": converter.is_output_lang
            }

            lang_dict[lang_code] = lang_specific_dict

        return lang_dict
