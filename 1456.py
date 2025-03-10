class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(s)
        #result = []
        current = sum(1 for ch in s[:k] if ch in vowels)
        maxv = current
        
        for i in range(k,n):
            if s[i] in vowels:
                current += 1

            if s[i -k] in vowels:
                current -= 1

            if current > maxv:
                maxv = current

        return maxv


        

            

        
