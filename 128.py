class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Early return for edge case
        if not nums:
            return 0

        # Use a set for O(1) lookups
        num_set = set(nums)
        longest = 0

        # Iterate through the numbers
        for num in num_set:
            # Only check the start of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                # Count consecutive elements
                while current + 1 in num_set:
                    current += 1
                    streak += 1

                # Update the longest streak
                longest = max(longest, streak)

        return longest
