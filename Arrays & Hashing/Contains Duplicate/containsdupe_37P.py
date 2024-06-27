class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        for count in nums_dict.values():
          if count > 1:
            return True
        return False
