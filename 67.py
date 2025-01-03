class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_A = int(a,2)
        int_B = int(b,2)

        sum_AB = int_A + int_B

        return bin(sum_AB)[2:]
         
