import main as main
from bootstrap import bootstrap

# Register all languages before testing can begin
bootstrap()

print(
    main.main("function s() {2}\nconsole.log(1)\n2\n3\n4\nfunction t() {5}",
              "js", "java"))
print(main.main("console.log(1)\n2\n3\n4", "js", "java"))
