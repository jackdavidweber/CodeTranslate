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
