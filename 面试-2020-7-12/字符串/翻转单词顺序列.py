"""
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。
后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""


# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        temp = [item for item in s]
        start = 0
        end = -1
        for index, item in enumerate(temp):
            if item == ' ':
                self.Reverse(temp, start, end)
                start = index + 1
                end = index
            else:
                end += 1
        self.Reverse(temp, start, end)
        self.Reverse(temp, 0, len(temp)-1)
        return "".join(temp)

    def Reverse(self, temp, low, high):

        while low < high:
            temp[low], temp[high] = temp[high], temp[low]
            low += 1
            high -= 1

s = "I am a student."
temp = [item for item in s]
solution = Solution()
solution.ReverseSentence(s)


