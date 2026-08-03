class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors=defaultdict(int)\

        for i in nums:
            colors[i]+=1

        nums[0:colors[0]]=[0]*colors[0]
        nums[colors[0]:colors[0]+colors[1]]=[1]*colors[1]
        nums[colors[0]+colors[1]:colors[0]+colors[1]+colors[2]]=[2]*colors[2]
