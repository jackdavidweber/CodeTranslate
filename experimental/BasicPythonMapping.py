
inputString =  '//'
inputLanguage = 'JavaScript'
outputLanguage = 'Python'

def translator(inputString, inputLanguage, outputLanguage):
  data = [{'#': ['Awk', 'BourneShell', 'Julia', 'Perl', 'Perl6', 'PHP', 'Python', 'YAML'], 
           '//': ['BCPL', 'C#', 'C++', 'F#', 'Go', 'Io', 'Java', 'JavaScript', 'PHP', 'Pike'], 
           '--': ['Ada', 'Cecil', 'Eiffel', 'Haskell', 'Lua', 'Sather', 'Simula', 'SQL92'], 
           ';': ['Assembler', 'Common Lisp', 'Emacs Lisp', 'Logo', 'MUMPS', 'Rebol', 'Scheme'], 
           '%': ['Erlang', 'Matlab', 'Mercury', 'Oz', 'PostScript', 'Prolog', 'TeX']}]
      
  for table in data:
    if inputString in table.keys():
      for key, languages in table.items():
        if outputLanguage in languages:
          return key


translation = translator(inputString, inputLanguage, outputLanguage)
print(translation) #Returns '#' (how you comment in Python)
