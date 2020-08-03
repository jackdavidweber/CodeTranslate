import translate


def matrix(self, code_objects):
    input_langs = []
    output_langs = []

    for obj in code_objects:
        if obj.get_input():
            input_langs.append(obj)
        if obj.get_output():
            output_langs.append(obj)

    for input_lang in input_langs:
        for output_lang in output_langs:
            inp = translate.translate(input_lang.get_code(),
                                      input_lang.get_lang(),
                                      output_lang.get_lang())
            self.assertEqual(output_lang.get_code(), inp)
