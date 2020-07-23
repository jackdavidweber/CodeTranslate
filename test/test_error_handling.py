import unittest2
import main


class TestErrorHandling(unittest2.TestCase):
    def test_class_unsupported(self):
        py_input = 'class Bar:\n\tdef __init__(self):\n\t\tpass'
        expected_error_obj = {'E0': {'errorType': 'unsupportedFeature', 'errorMessage': 'Feature not supported'}}

        self.assertEqual(expected_error_obj, main.main(py_input, 'py', 'js')['error'])


if __name__ == '__main__':
    unittest2.main()
