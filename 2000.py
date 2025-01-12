class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
       s = word.find(ch)
       if s == -1:
        return word
       else:
        result = word[s::-1] + word[s+1:]
        return result

