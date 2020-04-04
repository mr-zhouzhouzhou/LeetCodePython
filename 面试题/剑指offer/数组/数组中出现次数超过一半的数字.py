"""
数组中出现超过一般的数字



采用摩尔投票算法：
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers is None or len(numbers) == 0:
            return 0
        ma = numbers[0]
        count = 1
        for item in numbers[1:]:
            if ma == item:
                count += 1
            else:
                if count > 1:
                    count -= 1
                else:
                    count = 1
                    ma = item
        cnt = 0
        for item in numbers:
            if item == ma:
                cnt += 1
        return ma if cnt > len(numbers)//2 else 0


nums = [1,2,3,2,2,2,5,4,2]

soultion = Solution()

print(soultion.MoreThanHalfNum_Solution(nums))