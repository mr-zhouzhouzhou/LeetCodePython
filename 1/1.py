



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diction = {}
        for index, value in enumerate(nums):
            if value in diction.keys():
                diction[value] = diction[value] + [index]
            else:
                diction[value] = [index]
        print(diction)
        for index, value in enumerate(nums):
            start = index
            if (target - value) in diction.keys():
                if target - value == value :
                    if len(diction[value]) < 2:
                        continue
                    return diction[value][:2]
                else:
                    return [index, diction[target - value][0]]






if __name__ == '__main__':
    solution = Solution()
    nums = [3,3]
    target = 6
    print(solution.twoSum(nums, target))