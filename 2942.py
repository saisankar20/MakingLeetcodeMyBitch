class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        n = len(words)

        for i in range(n):
            if x in words[i]:
                result.append(i)
            else:
                continue
        return result
        
