class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''
        for char in s:
          if char.lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            continue
          else:
            palindrome += char.lower()
        if palindrome[::-1] == palindrome:
          return True
        else:
          return False
