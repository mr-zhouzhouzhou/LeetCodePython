"""
3种情况：
内劲为 inner_len, 外经是out_len
新来的长度为L
1： 小于内径：
      L <  inner_len
    那么： inner_len = inner_len - L
          out_len = out_len + L
2： inner_len < L <  out_len:
    那么： inner_len = 0
          out_len = out_len + L
3:  L > out_len
    那么： inner_len = L - out_len
          out_len = out_len + L
"""
def checkEdge(x, y, inner_len, out_len):
    length = x ** 2 + y ** 2
    if length >= inner_len ** 2 and length <= out_len ** 2:
        return True
    else:
        return False
def solution(nums, x, y):
    if x == 0 and y == 0:
        print(0)
        return
    inner_len = 0
    out_len = 0
    for index, L in enumerate(nums):
        if L > out_len:
            inner_len = L - out_len
            out_len = out_len + L
        elif L < inner_len:
            inner_len = inner_len - L
            out_len = out_len + L
        else:
            inner_len = 0
            out_len = out_len + L
        if checkEdge(x, y, inner_len, out_len):
            print(index + 1)
            return
    print(-1)
nums = [3,1,5,12]
solution(nums, 5, 5)
