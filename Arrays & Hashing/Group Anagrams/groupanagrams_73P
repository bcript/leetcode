class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for char in strs:
            sorted_strs.append(''.join(sorted(char)))

        anagrams = {}
        for index, char in enumerate(sorted_strs):
            if char not in anagrams:
                anagrams[char] = []
            anagrams[char].append(strs[index])
            
        return sorted(anagrams.values())
