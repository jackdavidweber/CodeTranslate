import unittest2
import translate


class TestErrorHandling(unittest2.TestCase):
    pass
    # def test_class_unsupported(self):
    #     py_input = 'class Bar:\n\tdef __init__(self):\n\t\tpass'
    #     expected_error_obj = {'E0': {'errorType': 'unsupportedFeature', 'errorMessage': 'Feature not supported'}}

    #     self.assertEqual(expected_error_obj, translate.translate(py_input, 'py', 'js')['error'])


if __name__ == '__main__':
    unittest2.main()
