import unittest2
import main

class TestJavaPrim(unittest2.TestCase):
    def test_basic(self):
        code = '''
        public class HelloWorld{
            public static void main(String []args){
                System.out.println();
            }
        }
        '''
        self.assertEqual("System.out.println()", main.main(code, 'java', 'java'))
    def test_basic_args(self):
        code = '''
        public class HelloWorld{
            public static void main(String []args){
                System.out.println("s");
                1;
            }
        }
        '''
        self.assertEqual('System.out.println("s")\n1', main.main(code, 'java', 'java'))

if __name__ == '__main__':
    unittest2.main()