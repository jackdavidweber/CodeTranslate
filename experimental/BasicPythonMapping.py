inputString =  '//'
inputLanguage = 'JavaScript'
outputLanguage = 'Python'

def translator(inputString, inputLanguage, outputLanguage):
  data = [{'#': ['Awk', 'BourneShell', 'CoffeeScript', 'E', 'FishShell', 'GNU-bc', 'GNU-sed', 'Icon', 'Io', 'Julia', 'Maple', 'merd', 'Perl', 'Perl6', 'PHP', 'Pliant', 'Python', 'Ruby', 'Tcl', 'YAML'], 
           '//': ['BCPL', 'C#', 'C++', 'C99', 'Dylan', 'F#', 'Go', 'Io', 'Java', 'JavaScript', 'PHP', 'Pike', 'Scilab', 'YCP', 'Yorick'], 
           '--': ['Ada', 'Cecil', 'Eiffel', 'Haskell', 'Lua', 'Sather', 'Simula', 'SQL92'], 
           ';': ['Assembler', 'Common Lisp', 'Emacs Lisp', 'Logo', 'MUMPS', 'Rebol', 'Scheme'], 
           '%': ['Erlang', 'Matlab', 'Mercury', 'Oz', 'PostScript', 'Prolog', 'TeX'], 
           'rem': ['Basic'], 
           "'": ['Visual Basic'], 
           '"': ['Vimscript'], 
           '\\': ['Forth'], 
           '!': ['Assembler', 'Fortran90'], 
           'NB.': ['J'], 
           'C or * in column 1': ['Fortran']}]
      
  for table in data:
    if inputString in table.keys():
      for key, languages in table.items():
        if outputLanguage in languages:
          return key


translation = translator(inputString, inputLanguage, outputLanguage)
print(translation) #Returns '#' (how you comment in Python)
