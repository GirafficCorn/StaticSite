
def extract_title(markdown):
    working = markdown.split("\n")
    for line in working:
        if line.startswith("#") and line[1] != "#":
            text = line.strip()
            text = text[2:]
            return text
    raise Exception("No header found")


