"""
Input: "I am a student."
Output: "student. a am I"
"""


"""
思路1: 先split， 然后合并
时间复杂度：O(n)
空间复杂度：O(n)
思路2：先反转字符串，然后再在小的上翻转字符串
时间复杂度：O(n),
空间复杂度：O(n)
"""


def solttion(s):

    s = list(s)
    low = 0
    high = len(s) - 1
    while low < high:

        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1
    low = 0
    high = 0
    for index in range(1, len(s)):
        if s[index] == " ":
            high = index -1
            while low < high:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
            low = index + 1
    return "".join(s)


print(solttion("I am a Student."))
