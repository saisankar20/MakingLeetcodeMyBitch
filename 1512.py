from collections import Counter
from typing import List  # Missing import added

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Initialize the count of good pairs to zero
        good_pairs_count = 0
      
        # Create a Counter object to track occurrences of each number
        occurrences = Counter()
      
        # Iterate over each number in the list
        for number in nums:
            # Add the current count of that number to good_pairs_count
            good_pairs_count += occurrences[number]
          
            # Increment the count for this number
            occurrences[number] += 1
      
        # Return the final count of good pairs
        return good_pairs_count
