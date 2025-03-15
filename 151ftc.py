class Solution:
    def reverseWords(self, s: str) -> str:
        res = re.split(r"(\s+)", s)
        res1 = res[::-1]

        result = ''.join(res1)
        return result
