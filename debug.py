import main as main
from bootstrap import bootstrap

# Register all languages before testing can begin
bootstrap()

print(main.main("function s() {2}\n console.log(1)", "js", "java"))