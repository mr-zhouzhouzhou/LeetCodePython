

# 4个数字 加减乘除  得到24


class Solution:
    def Game24Points(self , arr):
        # write code here
        nums = [0] * 7
        nums[0], nums[2], nums[4], nums[6] = arr[0], arr[1], arr[2], arr[3]


        for item in "+-*/":
            nums[1] = item
            for item in "+-*/":
                nums[3] = item
                for item in "+-*/":
                    nums[5] = item
                    if self.check_24(nums):
                        return True
        return False
    def check_24(self, nums):
        m_list = []
        index = 0
        while index < len(nums):
            if index in [1,3,5]:
                if nums[index] is "*" or nums[index] is "/":
                    if nums[index] is "*":
                        temp = m_list[-1] * nums[index+1]
                    else:
                        temp = m_list[-1] / nums[index + 1]
                    m_list.pop(-1)
                    m_list.append(temp)
                    index += 2
                else:
                    m_list.append(nums[index])
                    index += 1
            else:
                m_list.append(nums[index])
                index += 1
        count = m_list[0]
        index = 1
        while index < len(m_list):
            if m_list[index] == "+":
                count += m_list[index+1]
            if m_list[index] == "-":
                count -= m_list[index + 1]
            index += 2

        if count == 24:
            return True
        else:
            return False



solution = Solution()
nums = [7,2,1,10]
print(solution.Game24Points(nums))
