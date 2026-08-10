class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        max_profit=0
        size=len(prices)
        i=0
        j=1

        while i<size:
            sell=prices[i]
            while j<size and prices[i]<prices[j]:
                if prices[j]>=sell:
                    sell=prices[j]
                    j+=1
                else:
                    break;
                
            max_profit+=sell-prices[i]
            i=j
            j+=1

        return max_profit