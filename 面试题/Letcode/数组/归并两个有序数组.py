class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        if i < m:
            temp += nums1[i:m]
        if j < n:
            temp += nums2[j:n]
        return temp


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        flag = m + n - 1
        i = m - 1
        j = n - 1

        while i >=0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[flag] = nums1[i]
                i -= 1
            else:
                nums1[flag] = nums2[j]
                j -= 1
            flag -= 1
        if j >= 0:
            while j>=0:
                nums1[flag] = nums2[j]
                flag -= 1
                j -= 1
        print(nums1)

solution = Solution()

nums1 = [0]
m = 0
nums2 =[1]
n = 1

print(solution.merge(nums1, m, nums2, n))