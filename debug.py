import main as main
from bootstrap import bootstrap

# Register all languages before testing can begin
bootstrap()

print("****with functions****\n")
print(
    main.main("function s() {2}\nconsole.log(1)\n2\n3\n4\nfunction t() {5}",
              "js", "java"))
print("\n****with NO functions****\n")
print(main.main("console.log(1)\n2\n3\n4", "js", "java"))
