class Solution:
    def intToRoman1(self, num: int) -> str:#暴力法
        ret=''
        tmpVec= [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],  #个位
         ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],   #十位
         ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],    #百位
         ["", "M", "MM", "MMM"]];   #千位
        wei=0
        while(num!=0):
            temp=num%10
            ret=tmpVec[wei][temp]+ret
            num//=10
            wei+=1

        return ret

    def intToRoman(self, num: int) -> str:   #贪心算法
        # 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
        # 并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        index = 0
        res = ''
        while index < 13:
            # 注意：这里是等于号，表示尽量使用大的"面值"
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1
        return res

a=Solution()
num=58
print(a.intToRoman1(num))