from enum import Enum

class BlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    if not block:
        return BlockTypes.PARAGRAPH
    if block[0] == "#":
        limit = len(block)
        if " " not in block[0:6]:
            return BlockTypes.PARAGRAPH
        for i in range(0, min(6, limit)):
            if block[i] == "#" and block[i + 1] == " ":
                return BlockTypes.HEADING
            
    if block[:3] == "```" and block[-3:] == "```":
        return BlockTypes.CODE
    
    if block.startswith(">"):
        return BlockTypes.QUOTE
    
    if block.startswith("- "):
        check = block.split("\n")
        result = True
        for i in check:
            if i.startswith("- "):
                continue
            else:
                result = False
                break
        if result == True:
            return BlockTypes.UNORDERED_LIST
    
    if block[0].isdigit() and block[1:3] == ". ":
        check = block.split("\n")
        start = int(block[0])
        is_list = True
        for i in check:
            if int(i[0]) == start and i[1:3] == ". ":
                start += 1
            else:
                is_list = False
                break
        if is_list == True:
            return BlockTypes.ORDERED_LIST
    else:
        return BlockTypes.PARAGRAPH
            
