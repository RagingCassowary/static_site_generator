
def markdown_to_blocks(markdown):

    blocks = markdown.split("\n\n")

    stripped_blocks = list(map(lambda b: b.strip(), blocks))

    full_blocks = []

    for block in stripped_blocks:
        if block != "":
            full_blocks.append(block)
        
    return full_blocks
