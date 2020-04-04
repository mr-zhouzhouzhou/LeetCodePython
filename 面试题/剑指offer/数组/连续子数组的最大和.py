

class Solution:
    def FindGreatestSumOfSubArray(self, array):
            if array is None or len(array) == 0:
                return 0
            max = -9999999999
            count = 0
            for item in array:
                if count + item > item:
                    count = count + item
                elif count + item <= item:
                    count = item
                if count > max:
                    max = count
            return max

