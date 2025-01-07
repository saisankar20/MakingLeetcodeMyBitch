class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        output = []

        for i in range(len(words)):
            for j in range(i + 1 , len(words)):
                if words[i] in words[j]:
                    output.append(words[i])
                    break
        return output
