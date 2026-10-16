class Solution:
    def isPalindrome(self, s: str) -> bool:
        liste = [ch.lower() for ch in s if ch.isalnum()]
        return liste == liste[::-1]
        
        