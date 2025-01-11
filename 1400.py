class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
                return False

        fre = Counter(s)
        odd = sum(1 for  count in fre.values() if count % 2 != 0)

        return odd <= k
