from enum import Enum

class BlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    if block[0] == "#":
        limit = len(block)
        num_hashtag = 0
        for i in range(0, 6):
            if block[i] == "#":
                num_hashtag += 1
                if block[i + 1] == " ":
                    break
        if 1 <= num_hashtag <=6 and block[num_hashtag] == " ":
            return BlockTypes.HEADING
        else:
            return BlockTypes.PARAGRAPH
    elif block.strip().startswith("```") and block.strip().endswith("```"):
        return BlockTypes.CODE
    
    elif block.startswith(">"):
        return BlockTypes.QUOTE
    
    elif block.startswith("- "):
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
        else:
            return BlockTypes.PARAGRAPH
    
    elif block[0].isdigit() and block[1:3] == ". ":
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
    else:
        return BlockTypes.PARAGRAPH
            
