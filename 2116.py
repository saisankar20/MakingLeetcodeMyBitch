from collections import Counter

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If length is odd, it cannot be valid
        if len(s) % 2 != 0:
            return False

        # Left-to-right pass
        open_count = 0
        flexible_count = 0
        for i in range(len(s)):
            if locked[i] == '0':  # Flexible position
                flexible_count += 1
            elif s[i] == '(':
                open_count += 1
            else:  # s[i] == ')'
                open_count -= 1
            
            # If too many closing parentheses, use flexibility
            if open_count < 0:
                if flexible_count > 0:
                    flexible_count -= 1
                    open_count += 1  # Treat a flexible spot as '('
                else:
                    return False

        # Right-to-left pass
        close_count = 0
        flexible_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':  # Flexible position
                flexible_count += 1
            elif s[i] == ')':
                close_count += 1
            else:  # s[i] == '('
                close_count -= 1
            
            # If too many opening parentheses, use flexibility
            if close_count < 0:
                if flexible_count > 0:
                    flexible_count -= 1
                    close_count += 1  # Treat a flexible spot as ')'
                else:
                    return False

        return True
