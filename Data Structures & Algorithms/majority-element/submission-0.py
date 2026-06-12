class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        n=len(nums)
        for i in range(n):
            if not count.get(nums[i]):
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
            if count[nums[i]]>n//2:
                return nums[i]