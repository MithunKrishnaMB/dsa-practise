class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        items=set({})
        j=0

        for i in range(len(nums)):
            if i-j>k:
                items.remove(nums[j])
                j+=1

            if nums[i] in items:
                return True
            
            items.add(nums[i])
        
        return False