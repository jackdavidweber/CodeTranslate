import unittest2
import main

class TestLogStatement(unittest2.TestCase):
    def test_if(self):
        js_code = 'if (true) {\n\tconsole.log("This is true")\n}'
        py_code = 'if (True):\n\tprint("This is true")'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_else(self):
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else {\n\tconsole.log("1 is NOT true")\n}' # TODO: consider adding ; after console.log()
        py_code = 'if (1):\n\tprint("1 is true")\n else:\n\tprint("1 is NOT true")\n'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
   
    def test_elif(self):
        js_code = 'if (1) {\n\tconsole.log("1 is true")\n} else if (2) {\n\tconsole.log("2 is true")\n\tconsole.log("second line")\n}'
        py_code = 'if (1):\n\tprint("1 is true")\n elif (2):\n\tprint("1 is NOT true")\n\tprint("second line")\n'
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))

    def test_else(self):
        js_code = ''
        py_code = ''
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))
    
    def test_else(self):
        js_code = ''
        py_code = ''
        self.assertEqual(py_code, main.main(js_code, 'js', 'py'))
        self.assertEqual(js_code, main.main(py_code, 'py', 'js'))


    def test_if_else(self):
        js_code =

    def test_string_assign(self):
        self.assertEqual('x = "hi"', main.main('let x = "hi"', 'js', 'py'))
        self.assertEqual('let test = "working"', main.main('test = "working"', 'py', 'js'))
    
    def test_int_assign(self):
        self.assertEqual('num = 109', main.main('const num = 109', 'js', 'py'))
        self.assertEqual('let n = 12', main.main('n = 12', 'py', 'js'))
    
    def test_array_assign(self):
        self.assertEqual('arr = [3, 6]', main.main('let arr = [3, 6]', 'js', 'py'))
        self.assertEqual('let nest = [[1, 9], [2, 8]]', main.main('nest = [[1,9],[2,8]]', 'py', 'js'))
    
    def test_boolean_assign(self):
        self.assertEqual('boo = True', main.main('const boo=true', 'js', 'py'))
        self.assertEqual('let lean = false', main.main('lean = False', 'py', 'js'))

if __name__ == '__main__':
    unittest2.main()