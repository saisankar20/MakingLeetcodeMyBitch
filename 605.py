class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        
        for i in range(length):
            # Only consider empty spots:
            if flowerbed[i] == 0:
                # Check the left neighbor
                left_ok = (i == 0 or flowerbed[i - 1] == 0)
                # Check the right neighbor
                right_ok = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if left_ok and right_ok:
                    # Place a flower here
                    flowerbed[i] = 1
                    n -= 1
                    # If we've already placed n flowers, return True
                    if n <= 0:
                        return True
        
        # If we couldn't place enough flowers, return False
        return n <= 0
