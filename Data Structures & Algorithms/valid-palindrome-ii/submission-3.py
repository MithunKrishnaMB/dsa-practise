class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True
        
        l , r = 0 , len(s) - 1
        while l < r:
            if s[l] != s[r]:
                l2 = s[l+1:r+1]
                r2 = s[l:r]

                return l2 == l2[::-1] or r2 == r2[::-1]
            
            l , r = l + 1 , r - 1
        return True