class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size=len(numbers)
        for i in range(size):
            j=i+1
            while j<size:
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                j+=1
