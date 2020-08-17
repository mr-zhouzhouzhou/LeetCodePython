"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
# #         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        m_dict = []
        f(pRootOfTree, m_dict)
        if len(m_dict) == 0:
            return None
        if len(m_dict) == 0:
            m_dict[0].left = None
            m_dict[0].right = None
            return m_dict[0]
        head = m_dict[0]



    def f(self, pRootOfTree, m_dict):
        if pRootOfTree is None:
            return
        if pRootOfTree.left:
            self.f(pRootOfTree.left, m_dict)

        m_dict.append(pRootOfTree)
        if pRootOfTree.right:
            self.f(pRootOfTree.right, m_dict)














def soultion(nets, ips):
    pass










def f():
    n, m = map(int, input().split())
    m_dict = {}
    for _ in range(n):
        idc, net = map(str, input().split())
        nets = net.split('/')
        ips = nets[0].split(".")
        ips = convert(ips)
        m_dict[ips] = [int(nets[1]), int(idc)]
    for _ in range(m):
        ip = input().split(".")
        ip = convert(ip)
        max = [-1, -1]
        for item in m_dict.keys():
            length = checkLength(m_dict, item, ip)
            if length > max[0]:
                max = [length, m_dict[item][1]]
        print(max[1])

def convert(nums):
    IP = ""
    for num in nums:
        num = int(num)
        result = ['0'] * 8
        for i in range(8):
            if num % 2 == 0:
                result[-i - 1] = '0'
            else:
                result[-i - 1] = '1'
            num = num >> 1
        IP += ''.join(result)
    return IP

def checkLength(m_dict, item, ip):
    length = m_dict[item][0]
    for i in range(length):
        if item[i] != ip[i]:
            return -1
    return length

f()
"""
4 4
1 10.1.2.0/24
2 10.1.0.0/16
1 10.1.5.0/24
2 10.1.2.128/25
10.1.2.3
10.1.2.129
10.3.2.1
10.1.5.2
"""

