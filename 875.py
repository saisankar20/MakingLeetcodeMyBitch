class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(speed):
            total_hours = 0

            for pile in piles:
                total_hours += (pile + speed - 1)//speed
            return total_hours

        l, r = 1, max(piles)
        result = r

        while l <= r:
            m = (l + r)//2

            if hours(m) <= h:
                result = m
                r = m -1
            else:
                l = m + 1

        return result
