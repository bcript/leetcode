# Complexity of O(n^2)
# 3921ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterates over the first one
        for i in range(len(nums)):
        
          # iterates over the second index till the last
          for j in range(1, len(nums)):
        
            # if the index coincides, skip
            if i == j:
              continue
        
            # output
            else:
              if nums[i] + nums[j] == target:
                        return [i, j]
