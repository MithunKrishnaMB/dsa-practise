class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return is_pal(i + 1, j) or is_pal(i, j - 1)
            i += 1
            j -= 1

        return True