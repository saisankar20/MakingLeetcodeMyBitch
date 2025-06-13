from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # ── helper ──────────────────────────────────────────────
        def reverse(left: int, right: int) -> None:
            """Reverse nums[left … right] in-place."""
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left  += 1
                right -= 1
        # ── main routine ────────────────────────────────────────
        n = len(nums)
        k %= n                              # guard k ≥ n

        reverse(0, n - 1)                   # 1) reverse whole array
        reverse(0, k - 1)                   # 2) reverse first  k
        reverse(k, n - 1)                   # 3) reverse last n-k
