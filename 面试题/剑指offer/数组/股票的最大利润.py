


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices)< 2:
            return 0
        tmp = [0] * len(prices)
        max = 0
        for index in range(1, len(prices) + 1):
            if prices[-index] > max:
                tmp[-index] = prices[-index]
                max= prices[-index]
            else:
                tmp[-index] = max
        print(tmp)
        max = 0
        for index in range(len(prices)):
            if tmp[index] - prices[index] > max:
                max = tmp[index] - prices[index]
        return max


nums = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(nums))