import unittest2

loader = unittest2.TestLoader()
start_dir = './test'
suite = loader.discover(start_dir)

runner = unittest2.TextTestRunner()
runner.run(suite)