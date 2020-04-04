"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
"""

"""
思路： 从左下角开始遍历，往上走是变小，往右走是变大

"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        m = row - 1
        n = 0

        while m >= 0 and n < col:
            if array[m][n] > target:
                m -= 1
            elif array[m][n] < target:
                n += 1
            else:
                return True
        return False


target = 9
array = [[1,2,3,4,5],
         [4,5,6,7,8],
         [5,6,7,9,10]]
