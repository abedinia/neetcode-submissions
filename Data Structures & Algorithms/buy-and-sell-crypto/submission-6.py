class Solution:
    def check_value(self, first_day: int, all_days: List[int]) -> int:
        if len(all_days) == 0:
            return 0
        
        max_val = max(all_days) - first_day
        if max_val != 0:
            return max_val

        return 0

    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i, v in enumerate(prices):
            max_val = self.check_value(v, prices[i+1:])
            
            if  max_val > result:
                result = max_val
        
        return result