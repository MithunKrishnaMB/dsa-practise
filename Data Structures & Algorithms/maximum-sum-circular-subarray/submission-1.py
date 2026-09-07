class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        
        max_sum=nums[0]
        cur_max=nums[0]

        min_sum=nums[0]
        cur_min=nums[0]

        for i in nums[1:]:
            cur_max=max(i,cur_max+i)
            max_sum=max(max_sum,cur_max)

            cur_min=min(i,cur_min+i)
            min_sum=min(min_sum,cur_min)
        
        if max_sum<0:
            return max_sum

        return max(max_sum,total_sum-min_sum)