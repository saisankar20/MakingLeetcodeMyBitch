class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        r = [""]
        for word in words:
            if word == word[::-1]:
                return word
        return r[0]
