class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items=set({})
        for i in nums:
            if i in items:
                return True
            else:
                items.add(i)
        return False