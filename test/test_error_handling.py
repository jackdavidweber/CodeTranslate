import unittest2
import main


class TestErrorHandling(unittest2.TestCase):

    def test_class_unsupported(self):
        code_input = 'class Bar:\n\tdef __init__(self):\n\t\tpass'
        response = main.main(code_input, 'py', 'js')

        expected_error_obj = {
            'E0': {
                'errorType': 'unsupportedFeature',
                'errorMessage': 'Feature not supported'
            }
        }
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = '$$E0$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_supported_and_unsupported_features(self):
        code_input = 'class Bar:\n\tdef __init__(self):\n\t\tpass\nprint()\nclass Foo:\n\tdef __init__(self):\n\t\tpass'
        response = main.main(code_input, 'py', 'js')

        expected_error_obj = {
            'E0': {
                'errorType': 'unsupportedFeature',
                'errorMessage': 'Feature not supported'
            },
            'E1': {
                'errorType': 'unsupportedFeature',
                'errorMessage': 'Feature not supported'
            },
        }
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = '$$E0$$\nconsole.log()\n$$E1$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_input_language_unsupported(self):
        code_input = 'print()'
        response = main.main(code_input, 'unknown language', 'js')

        expected_error_obj = {
            'E0': {
                "errorType": "invalidArguments",
                "errorMessage": "arguments not valid"
            }
        }
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = '$$E0$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_output_language_unsupported(self):
        code_input = 'print()'
        response = main.main(code_input, 'py', 'unknown language')

        expected_error_obj = {
            'E0': {
                "errorType": "invalidArguments",
                "errorMessage": "arguments not valid"
            }
        }
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = '$$E0$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_no_args(self):
        response = main.main()

        expected_error_obj = {
            'E0': {
                "errorType": "invalidArguments",
                "errorMessage": "arguments not valid"
            }
        }
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = '$$E0$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_impossible_translation_bash(self):
        # Note that bash does not support nested arrays
        code_input = 'print([[1]])'
        response = main.main(code_input, 'py', 'bash')

        expected_error_obj = {
            'E0': {
                "errorType":
                    "impossibleTranslation",
                "errorMessage":
                    "direct translation does not exist to this language"
            }
        }
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = 'echo $$E0$$'
        self.assertEqual(expected_output_str, response['translation'])

    def test_impossible_translation_java(self):
        #Note that java does not support arrays with multiple types
        code_input = 'print([1, "hello world"])'
        response = main.main(code_input, 'py', 'java')

        expected_error_obj = {
            'E0': {
                "errorType":
                    "impossibleTranslation",
                "errorMessage":
                    "direct translation does not exist to this language"
            }
        }
        self.assertEqual(expected_error_obj, response['error'])

        expected_output_str = 'System.out.println(Arrays.toString(new $$E0$$ {1, "hello world"}));'
        self.assertEqual(expected_output_str, response['translation'])


if __name__ == '__main__':
    unittest2.main()
