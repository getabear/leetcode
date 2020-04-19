class Solution1:
    def countPrimes(self, n: int) -> int:
        #暴力法 超时
        def judge(num):
            if num<=1:
                return False
            for i in range(2,num):
                if num%i==0:
                    return False
            return True

        count=0
        for i in range(2,n):
            if judge(i):
                count+=1
        return count

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        nmap=[1]*n
        nmap[0]=0
        nmap[1]=0

        for i in range(2,int(n**0.5)+1):
            if nmap:
                nmap[i*i:n:i]=[0]*len(nmap[i*i:n:i])
        return sum(nmap)


a=Solution1()
print(a.countPrimes(10))