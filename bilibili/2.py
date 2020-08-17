


class Solution:
    def IsValidExp(self, s):

        if s is None:
            return False
        length = len(s)
        if length == 0:
            return True
        if length % 2 == 1:
            return False
        m_list = []
        for item in s:
            if item is '{' or item is '[' or item is '(':
                m_list.insert(0, item)

            elif item is ']' or item is '}' or item is ')':
                if len(m_list) == 0:
                    return False
                if item == ']' and m_list[0] != "[":
                    return False
                if item == '}' and m_list[0] != "{":
                    return False
                if item == ')' and m_list[0] != "(":
                    return False
                m_list.pop(0)
            else:
                return False

        if len(m_list) == 0:
            return True
        return False



solution = Solution()

s = ""
print(solution.IsValidExp(s))

