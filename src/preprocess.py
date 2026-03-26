import re


def preprocess(source: str) -> str:
    # Some competitive-programming datasets emit operators with spaces around them
    source = source.replace(' > = ', ' >= ')
    source = source.replace(' < = ', ' <= ')
    source = source.replace(' ! = ', ' != ')
    source = source.replace(' * * ', ' ** ')
    source = source.replace(' / / ', ' // ')

    # Convert Python 2 print statements to function calls.
    # Stops at '#' so inline comments aren't pulled into the argument list.
    # A trailing comma (print x,) maps to end="" to suppress the newline,
    # matching Python 2's behaviour.
    # Caveat: a '#' inside a string literal will truncate the match early —
    # acceptable for the competitive-programming code this tool processes.
    def fix_print(m: re.Match) -> str:
        content = m.group(1).rstrip()
        if content.endswith(','):
            content = content[:-1].rstrip() + ', end=""'
        return f'print({content})'

    source = re.sub(r'\bprint\s+(?!\()([^#\n]*)', fix_print, source)
    return source
