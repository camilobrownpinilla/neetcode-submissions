class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "".join(c for c in s if c.isalnum()).lower()
        return valid == valid[::-1]
        