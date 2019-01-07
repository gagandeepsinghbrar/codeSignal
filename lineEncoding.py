def lineEncoding(s):
    return re.sub(r'(.)(\1+)', lambda char: str(len(char.group())) + char.group(1),s)

