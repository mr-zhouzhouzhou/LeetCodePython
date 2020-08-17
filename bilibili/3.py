#
#
# @param N int整型
# @return int整型
#


#  最少多少个硬币

#  1， 4， 16 ， 64
class Solution:
    def GetCoinCount(self , N):
        # write code here
        N = 1024 - N
        count = 0
        m_list = [64, 16, 4, 1]
        while N > 0:
            a = N // m_list[0]
            if a > 0:
                N = N - a * m_list[0]
                count += a
            m_list.pop(0)
        return count

solution = Solution()
print(solution.GetCoinCount(200))