class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_sum = 0
        best_sum = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] + running_sum >= 0:
                running_sum += prices[i] - prices[i-1]
            else:
                running_sum = 0
            if running_sum > best_sum:
                best_sum = running_sum
        return best_sum
                
        