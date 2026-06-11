class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp={}

        for i,num in enumerate(nums):
            if target-num in comp:
                return [comp[target-num],i]
            else:
                comp[nums[i]]=i