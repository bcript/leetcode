class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for cur in range(len(nums)):
             x = target - nums[cur]
             if x in nums and nums.index(x) != cur:
                return [nums.index(x), cur]
