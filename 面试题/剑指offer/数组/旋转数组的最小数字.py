

"""
旋转数组的最小值：

"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        pass
        if rotateArray is None:
            return None
        if len(rotateArray) == 1:
            return rotateArray[0]

        start = 0
        end = len(rotateArray) - 1
        middle = (start + end) // 2
        while start <= end:
            if rotateArray[middle] > rotateArray[middle + 1]:
                return rotateArray[middle + 1]
            elif rotateArray[middle] > rotateArray[end]:
                start = middle + 1
            else:
                end = middle - 1

        return -1