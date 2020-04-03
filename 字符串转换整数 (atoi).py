import re
class Solution1:
    def myAtoi(self, str: str) -> int:
        flag=0    #0为正数
        nums="1234567890"
        length=len(str)
        if length==0:
            return 0
        ret=0
        for index,s in enumerate(str):
            if s==' ':
                continue
            if (s=='-' or s=='+') :
                if s=='-':
                    flag=1
                else:
                    flag=0
                if index==length-1:
                    return 0
                if str[index+1] in nums:
                    i=index+2
                    while i<=length:
                        try:
                            ret=int(str[index+1:i])
                        except:
                            break
                        i+=1
                    if flag:
                        ret=-ret
                    if ret < -2147483648:
                        return -2147483648
                    if ret > 2147483647:
                        return 2147483647
                    return ret
            if s in nums:
                i=index+1
                while i<=length:
                    try:
                        ret=int(str[index:i])
                    except:
                        break
                    i += 1
                if ret < -2147483648:
                    return -2147483648
                if ret > 2147483647:
                    return 2147483647
                return ret
            else:
                return 0
        return 0

    def myAtoi2(self, str: str) -> int:   #大佬写的正则表达式的解法
        return max(min(int(*re.findall("^[\+,\-]?\d+",str.lstrip())),(1<<31)-1),-(1<<31))
'''
    lstrip()方法会返回一个字符串,会去除前面的空格
    以下实例展示了lstrip()
    的使用方法：

    str = "     this is string example....wow!!!     ";
    print
    str.lstrip();
    str = "88888888this is string example....wow!!!8888888";
    print
    str.lstrip('8');
    以上实例输出结果如下：

    this is string example....wow!!!
    this is string example....wow!!!8888888
'''


# 状态机解法
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans


a=Solution()
print(a.myAtoi("-3.14159"))
a=[1,2,3,4]

