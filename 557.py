class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        revword = []

        for word in words:
            revword.append(word[::-1])
           


        return ' '.join(revword)

        

        
