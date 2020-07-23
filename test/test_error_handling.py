import unittest2
import main


class TestErrorHandling(unittest2.TestCase):
    def test_class_unsupported(self):
        py_input = 'class Bar:\n\tdef __init__(self):\n\t\tpass'
        response = main.main(py_input, 'py', 'js')

        expected_error_obj = {'E0': {'errorType': 'unsupportedFeature', 'errorMessage': 'Feature not supported'}}
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = '$$E0$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_supported_and_unsupported_features(self):
        py_input = 'class Bar:\n\tdef __init__(self):\n\t\tpass\nprint()\nclass Foo:\n\tdef __init__(self):\n\t\tpass'
        response = main.main(py_input, 'py', 'js')

        expected_error_obj = {
            'E0': {'errorType': 'unsupportedFeature', 'errorMessage': 'Feature not supported'},
            'E1': {'errorType': 'unsupportedFeature', 'errorMessage': 'Feature not supported'},
            }
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = '$$E0$$\nconsole.log()\n$$E1$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_input_language_unsupported(self):
        expected_error_obj = {'E0': {"errorType": "invalidArguments", "errorMessage": "arguments not valid"}}
        self.assertEqual(expected_error_obj, main.main('print()', 'unknown language', 'js'))

        expected_output_str = '$$E0$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_output_language_unsupported(self):
        expected_error_obj = {'E0': {"errorType": "invalidArguments", "errorMessage": "arguments not valid"}}
        self.assertEqual(expected_error_obj, main.main('print()', 'py', 'unknown language'))

        expected_output_str = '$$E0$$'
        self.assertEqual(expected_output_str, response['translation'])

if __name__ == '__main__':
    unittest2.main()
