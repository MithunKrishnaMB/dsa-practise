class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        total = 0
        j = 0

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                min_len = min(min_len, i - j + 1)
                total -= nums[j]
                j += 1

        return 0 if min_len == float("inf") else min_len