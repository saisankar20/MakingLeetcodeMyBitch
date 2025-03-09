class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) != (str2 + str1):
            return ""

        def gcd_length(a, b):
            if b > a:
                a , b = b, a
            while b != 0:
                a , b = b, a % b
            return a

        len_str1 = len(str1)
        len_str2 = len(str2)
        g = gcd_length(len_str1, len_str2)

        return str1[:g]





        
