


"""
这是一个排序问题

"""
class Solution:
    def PrintMinNumber(self, numbers):
# write code here
        if numbers is None or len(numbers) == 0:
            return ""
        length = len(numbers)
        for i in range(0, length -1):
            for j in range(i, length):
                self.check(numbers, i, j)
        count = ""
        for item in numbers:
            count += str(item)
        return count

    def check(self, numbers, num1, num2):

        if str(numbers[num1]) + str(numbers[num2]) > str(numbers[num2]) + str(numbers[num1]):
            numbers[num1], numbers[num2] = numbers[num2], numbers[num1]




nums = [3, 32, 321]
soultion = Solution()
s = soultion.PrintMinNumber(nums)
print(s)