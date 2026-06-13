class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=k

        if j>=len(nums):
            items=set({})
            for x in range(i,j):
                if nums[x] in items:
                    return True
                items.add(nums[x])
        else:
            while j<len(nums):
                items=set({})
                for x in range(i,j+1):
                    if nums[x] in items:
                        return True
                    items.add(nums[x])
                
                i+=1
                j+=1
        
        return False