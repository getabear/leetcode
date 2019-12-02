import re
class Solution:
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



a=Solution()
print(a.myAtoi2("  -1234fgsd"))
a=[1,2,3,4]

