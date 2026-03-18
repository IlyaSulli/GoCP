import re

def preprocess(source):
    # Fix spaced operators
    source = source.replace(' > = ', ' >= ')
    source = source.replace(' < = ', ' <= ')
    source = source.replace(' ! = ', ' != ')
    source = source.replace(' * * ', ' ** ')
    source = source.replace(' / / ', ' // ')
    # Fix Python 2 print statements: print "x" -> print("x")
    # Also handles trailing comma: print "x", -> print("x", end="")
    def fix_print(m):
        content = m.group(1).rstrip()
        if content.endswith(','):
            content = content[:-1].rstrip() + ', end=""'
        return f'print({content})'
    source = re.sub(r'\bprint\s+(?!\()(.*)', fix_print, source)
    return source