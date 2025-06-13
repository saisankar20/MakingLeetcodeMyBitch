from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        # Left → right pass
        count = 0
        for i in range(1, n):
            if boxes[i - 1] == '1':
                count += 1
            ans[i] = ans[i - 1] + count

        # Right → left pass
        count = 0
        s = 0
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                count += 1
            s += count
            ans[i] += s

        return ans
