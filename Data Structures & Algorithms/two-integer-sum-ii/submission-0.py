class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        comp={}
        for i,n in enumerate(numbers):
            if target-n in comp:
                return [comp[target-n]+1,i+1]
            else:
                comp[n]=i
        return [-1,-1]