def formatString(input):
    # pick a word and make sure it is a truthy value, well if it is keep it and join on         spaces
    return " ".join(list(filter(lambda word : word, input.split(" "))))


