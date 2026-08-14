class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            current_weight = 0
            required_days = 1

            for weight in weights:
                if current_weight + weight > mid:
                    required_days += 1
                    current_weight = 0

                current_weight += weight

            if required_days > days:
                low = mid + 1
            else:
                high = mid

        return low