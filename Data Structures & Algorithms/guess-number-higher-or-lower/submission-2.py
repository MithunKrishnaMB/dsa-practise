class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2

            num = guess(mid)

            if num == 0:
                return mid
            elif num == 1:
                low = mid + 1
            else:
                high = mid - 1