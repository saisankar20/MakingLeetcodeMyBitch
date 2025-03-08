class Solution:
   def minWindow(self, s: str, t: str) -> str:
       s_count, t_count = Counter(), Counter(t)
       l = 0
       results = ""

       for r in range(len(s)):
           s_count[s[r]] += 1
           while (s_count & t_count == t_count):
               if len(s[l:r+1]) < len(results) or results == "":
                    results = s[l:r+1]
               s_count[s[l]] -= 1 
               l += 1
       return results
