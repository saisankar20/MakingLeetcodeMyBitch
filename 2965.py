class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        ans = []
        n = len(grid)

        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                if num in seen:
                    ans.append(num)
                seen.add(num)
                

        sorted_seen = sorted(seen)
        missing_found = False

        for i in range(len(sorted_seen) - 1):
            if sorted_seen[i+1] != sorted_seen[i]+ 1:
                ans.append(sorted_seen[i]+ 1)
                missing_found = True
                break

        if not missing_found:
            expected_total = n * n
            for num in range(1, expected_total + 1):
                if num not in seen:
                    ans.append(num)
                    break
        
        return ans


        
