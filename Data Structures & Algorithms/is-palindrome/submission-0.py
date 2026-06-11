class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars=""
        for i in s:
            if i.isalnum():
                chars+=i.lower()
        return chars==chars[::-1]