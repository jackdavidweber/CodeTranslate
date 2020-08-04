import unittest
import tempfile
import app as flaskr
import os
import pytest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_get_request(self):
        rv = self.app.get('/')
        assert b'js' in rv.data
        assert b'py' in rv.data
        assert b'bash' in rv.data
        assert b'java' in rv.data

    def test_hello_world(self):
        rv = self.app.post('/',
                           data=dict(input='console.log("hello world")',
                                     in_lang='js',
                                     out_lang='py'))
        assert b'print(\\"hello world\\")' in rv.data

    def test_java_bash(self):
        rv = self.app.post('/',
                           data=dict(input='System.out.println(1);',
                                     in_lang='java',
                                     out_lang='bash'))
        assert b'echo 1' in rv.data

    def test_auto_py_to_js(self):
        rv = self.app.post('/',
                           data=dict(input='def test():\n\t1',
                                     in_lang='auto',
                                     out_lang='js'))
        assert b'function test() {\\n\\t1\\n}' in rv.data

    def test_auto_js_to_py(self):
        rv = self.app.post('/',
                           data=dict(input='let x = 3;',
                                     in_lang='auto',
                                     out_lang='py'))
        assert b'x = 3' in rv.data
