class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float("inf")
        sum=0
        j=0

        for i in range(len(nums)):
            sum+=nums[i]
            
            if sum>=target:
                while sum>=target:
                    sum-=nums[j]
                    j+=1
                min_len=min(min_len,i-j+2)
        
        if min_len==float("inf"):
            return 0
        else:
            return min_len