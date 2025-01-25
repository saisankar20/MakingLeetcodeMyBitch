import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
       
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0

        def count_soldiers(row: List[int]) -> int:
         
            low, high = 0, n
            while low < high:
                mid = (low + high) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low
        
       
        soldier_counts = []
        for i in range(m):
            sc = count_soldiers(mat[i])
            soldier_counts.append((sc, i))
        
        
        k_weakest = heapq.nsmallest(k, soldier_counts)
        
        
        return [row_idx for _, row_idx in k_weakest]
