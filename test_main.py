import unittest2

loader = unittest2.TestLoader()
directory = './test'
suite = loader.discover(directory)

runner = unittest2.TextTestRunner()
runner.run(suite)