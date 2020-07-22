import main
from bootstrap import bootstrap

# Register all languages before testing can begin
bootstrap()

print(main.main('print(1)', 'py', 'js'))