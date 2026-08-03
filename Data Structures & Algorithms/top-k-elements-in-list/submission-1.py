class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=dict(Counter(nums))

        count=list(frequency.items())
        count.sort(key=lambda x:x[1],reverse=True)

        result=[]

        for i in range(k):
            result+=[count[i][0]]

        return result