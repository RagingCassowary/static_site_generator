from blocktype import BlockType

def block_to_blocktype(block):
    if block[0] == "#":
        return BlockType.HEADING
    if block[0:4] == "```\n" and block[-3:len(block)] == "```":
        return BlockType.CODE
    if block[0] == ">":
        return BlockType.QUOTE
    if block[0] == "-":
        lines = block.split("\n")
        for line in lines:
            if line[0:2] != "- ":
                raise Exception("invalid markdown for unordered list")
        return BlockType.UNORDERED_LIST
    if block[0:3] == "1. ":
        lines = block.split("\n")
        counter = 1
        for line in lines:
            if line[1:3] != ". " or line[0] != str(counter):
                raise Exception("invalid markdown for ordered list")
            counter += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH