class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp={}

        for i in range(len(nums)):
            if target-nums[i] in comp:
                return [comp[target-nums[i]],i]
            else:
                comp[nums[i]]=i
        
        return []