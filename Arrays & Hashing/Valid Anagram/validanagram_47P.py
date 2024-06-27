class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {}
        chars_t = {}
        for char in s:
          chars_s[char] = chars_s.get(char, 0) + 1
        for char in t:
          chars_t[char] = chars_t.get(char, 0) + 1
        if chars_t  == chars_s:
            return True
        else:
            return False
        
