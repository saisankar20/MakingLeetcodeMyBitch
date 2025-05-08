from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or not nums:
            return []

        dq   = deque()   # stores indices, ALWAYS in decreasing nums[idx] order
        ans  = []

        for i, x in enumerate(nums):

            # 1️⃣ Eject indices that fell out of the window (too far left)
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2️⃣ Maintain decreasing order from left→right
            while dq and nums[dq[-1]] < x:
                dq.pop()

            dq.append(i)

            # 3️⃣ Once the first window is complete, record its max each step
            if i >= k - 1:
                ans.append(nums[dq[0]])   # leftmost index == current maximum

        return ans
