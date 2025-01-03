class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        rem = salary[1:-1]
        avg = sum(rem) / len(rem)

        return avg



        
