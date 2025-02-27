class MaxProfit:
    def two_pointers(self, prices) -> int:
        l,r = 0,1
        max_p = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > max_p:
                    max_p = profit
            else:
                l = r
            r += 1
        return max_p

    def max_min(self, prices) -> int:
        if not prices:
            return 0
            
        max_p = 0
        min_b = prices[0]
        for sell in prices:
            max_p = max(max_p, sell - min_b)
            min_b = min(min_b, sell)
        return max_p