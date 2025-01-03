class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Number_Words = s.split()
        x = len(Number_Words)

        return len(Number_Words[x-1])



        
