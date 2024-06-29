class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''
        for char in s:
          if char.isalpha() or char.isdigit():
            palindrome += char.lower()
        if palindrome[::-1] == palindrome:
          return True
        else:
          return False
