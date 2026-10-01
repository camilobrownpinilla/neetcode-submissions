class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_string = ''
        for char in s:
            if char.isalnum():
                normalized_string += char.lower()
        return normalized_string == normalized_string[::-1]