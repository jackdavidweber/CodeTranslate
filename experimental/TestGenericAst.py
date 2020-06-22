import unittest2
import GenericAstTesting

class TestPythonToPython(unittest2.TestCase):

    def test_print_statment_no_args(self):
        self.assertEqual('print(\'\')', GenericAstTesting.codeTranslate('TestPythonFiles/EmptyPrint.py'))
    
    def test_print_string_args(self):
        self.assertEqual('print(\'Hello World!\')', GenericAstTesting.codeTranslate('TestPythonFiles/StringPrint.py'))
    
    def test_variable_dec(self):
        expected = "x = 5\nstring = \'string\'"
        self.assertEqual(expected, GenericAstTesting.codeTranslate('TestPythonFiles/VariableDeclaration.py'))
    

if __name__ == '__main__':
    unittest2.main()