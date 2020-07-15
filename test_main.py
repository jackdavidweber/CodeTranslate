import unittest2
from bootstrap import bootstrap

# Register all languages before testing can begin
bootstrap()

loader = unittest2.TestLoader()
directory = './test'
suite = loader.discover(directory)

runner = unittest2.TextTestRunner()
runner.run(suite)