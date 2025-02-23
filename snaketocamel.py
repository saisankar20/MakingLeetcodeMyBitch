import re

def solution(src):
    def convert_snake_to_camel(match):
        word = match.group(0)
        if word.count('_') == len(word):  # If the entire word is underscores, return as is
            return word
        
        leading_underscores = re.match(r"^_+", word)
        trailing_underscores = re.search(r"_+$", word)
        core_part = word.strip("_")
        
        if "_" in core_part:
            parts = core_part.split('_')
            core_part = parts[0] + ''.join(part.capitalize() for part in parts[1:])
        
        leading_underscores = leading_underscores.group() if leading_underscores else ""
        trailing_underscores = trailing_underscores.group() if trailing_underscores else ""
        
        return leading_underscores + core_part + trailing_underscores
    
    return re.sub(r'\b_?[a-z]+(?:_[a-z]+)*_?\b', convert_snake_to_camel, src)
