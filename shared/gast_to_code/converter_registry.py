class ConverterRegistry():
    converters = {}

    @staticmethod
    def register(converter, lang_code):
        ConverterRegistry.converters[lang_code] = converter

    @staticmethod
    def get_converter(lang_code):
        return ConverterRegistry.converters[lang_code]

    @staticmethod
    def get_language_codes_by_property(prop, is_complement=False):
        """
        Returns supported language codes in the converter as a list of strings.
        prop is a string representing the property that the languages should be gotten by
            For example, get_language_codes_by_property("is_beta") would return a list of beta languages.
        is_complement is a boolean representing whether or not the complement of the prop should be returned
            For example, get_language_codes_by_property("is_beta", True) would return a list of non-beta languages.
        """
        all_lang_codes = ConverterRegistry.converters.keys()
        subset_lang_codes = []
        for lang_code in all_lang_codes:
            converter = ConverterRegistry.get_converter(lang_code)
            if getattr(converter, prop):
                subset_lang_codes.append(lang_code)

        if is_complement:
            return (list(set(all_lang_codes) - set(subset_lang_codes)))
        else:
            return subset_lang_codes

    @staticmethod
    def get_lang_dict():
        """
        Returns a dictionary where keys are language codes are dicts
        with pretty names, and booleans indicating information about whether 
        the language is in beta, supports input and supports output
        """
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
