class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 6:
            return index
        dp = [1] * index
        i2, i3, i5 = 0, 0, 0
        for i in range(1, index):
            next2, next3, next5 = dp[i2] * 2, dp[i3]*3, dp[i5]*5
            dp[i] = min(next2, min(next3, next5))
            if dp[i] == next2:
                i2 += 1
            if dp[i] == next3:
                i3 += 1
            if dp[i] == next5:
                i5 += 1
        print(dp)
        return dp[index - 1]


soultion = Solution()
re = soultion.GetUglyNumber_Solution(7)

print(re)