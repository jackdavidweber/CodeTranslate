import translate


def test(self, py_code, js_code, java_code=None, bash_code=None):
    if bash_code:
        self.assertEqual(bash_code, translate.translate(py_code, 'py', 'bash'))
        self.assertEqual(bash_code, translate.translate(js_code, 'js', 'bash'))
    if java_code:
        self.assertEqual(java_code, translate.translate(js_code, 'js', 'java'))
        self.assertEqual(js_code, translate.translate(java_code, 'java', 'js'))
        self.assertEqual(py_code, translate.translate(java_code, 'java', 'py'))
        self.assertEqual(java_code, translate.translate(py_code, 'py', 'java'))

    self.assertEqual(py_code, translate.translate(js_code, 'js', 'py'))
    self.assertEqual(js_code, translate.translate(py_code, 'py', 'js'))

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
            self.assertEqual(output_lang.get_code(), translate.translate(input_lang.get_code(), input_lang.get_lang(), output_lang.get_lang()))
