
class Solution:
    def romanToInt(self, s: str) -> int:
        def fun1(s):     #第一种方法,效率低,只击败了18%的人
            tmpVec= [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],  #个位
             ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],   #十位
             ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],    #百位
             ["", "M", "MM", "MMM"]];
            start = 0
            end = 1
            temp = 3
            num = 0
            index = 0
            times = 1000
            length=len(s)
            while(temp!=-1):
                while(s[start:end] in tmpVec[temp] and end<=length):
                    end+=1
                index=tmpVec[temp].index(s[start:end-1])
                num=num+times*index
                start=end-1
                times//=10
                temp-=1
            return num

        def fun2(s):
            # I 可以放在 V (5)和 X (10) 的左边，来表示4和9。
            # X 可以放在 L (50)和 C (100)的左边，来表示 40和 90。 
            # C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
            num=0
            map={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,
                 'L':50,'XL':40,'X':10,'IX':9,
                 'V':5,'IV':4,'I':1
                 }   #初始化哈希表
            length=len(s)
            index=0
            while(index<length):
                if(map.get(s[index:index+2]) is not None):
                    num+=map[s[index:index+2]]
                    index+=2
                else:
                    num+=map[s[index:index+1]]
                    index+=1
            return num


        return fun2(s)

a=Solution()
s="IX"
print(a.romanToInt(s))
