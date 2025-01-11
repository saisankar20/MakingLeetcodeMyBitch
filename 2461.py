class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        window_sum = 0
        max_sum = 0
        seen = set()

        for r in range(len(nums)):
            # Remove elements from the left until there are no duplicates
            while nums[r] in seen:
                seen.remove(nums[l])
                window_sum -= nums[l]
                l += 1

            # Add the current element to the set and the window sum
            seen.add(nums[r])
            window_sum += nums[r]

            # Check if the window size is exactly k
            if r - l + 1 == k:
                max_sum = max(max_sum, window_sum)

                # Slide the window forward by removing the leftmost element
                seen.remove(nums[l])
                window_sum -= nums[l]
                l += 1

        return max_sum
