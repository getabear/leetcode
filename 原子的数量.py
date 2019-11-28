class Solution:
    def countOfAtoms(self, formula: str) -> str:
        ch = [chr(i) for i in range(65, 91)]   #大写
        xiao=[chr(i) for i in range(97,123)]   #小写
        shu=[chr(i) for i in range(48,58)]      #数字
        ret={}
        formula="("+formula+")"
        def n_of_xiao(formula):
            num = 0
            for i in formula:
                if i not in xiao:
                    break
                num += 1  # 小写字母个数
            return num

        def n_of_shu(formula):
            temp = 0
            for i in formula:
                if i not in shu:
                    break
                temp += 1  # 数字个数
            return temp

        def fun(formula,ret):    #解决没有括号的化学式
            num=0
            if(len(formula)==0):
                return 0
            elif(formula[0] in ch):   #大写开头
                num=n_of_xiao(formula[1:])
                str=formula[0:num+1]
                temp=0
                temp=n_of_shu(formula[num+1:])
                if(temp==0):
                    if(str in ret.keys()):
                        ret[str]+=1
                    else:
                        ret.setdefault(str,1)
                else:
                    if(str in ret.keys()):
                        ret[str]+=int(formula[num+1:num+1+temp])
                    else:
                        ret.setdefault(str,int(formula[num+1:num+1+temp]))
                fun(formula[num+1+temp:],ret)

        result = {}
        def fun2(formula,str):
            length=len(formula)
            index=0
            count=0
            while(index<length):
                if formula[index] =="(":
                    count=fun2(formula[index+1:],"")
                    index+=count
                elif formula[index]==")":
                    num=n_of_shu(formula[1+index:])
                    wei=num
                    count=num+index+1
                    if(num!=0):
                        num=int(formula[index+1:index+1+num])
                    else:
                        num=1
                    times=0
                    i=wei+index
                    while(i<length):
                        if(formula[i]=="("):
                            times-=1
                        elif(formula[i]==")"):
                            times+=1
                            if(times==1):
                                temp=n_of_shu(formula[i+1:])
                                if(temp!=0):
                                    temp=int(formula[i+1:i+1+temp])
                                else:
                                    temp=1
                                num*=temp
                                times=0
                        i+=1
                    result.setdefault(str,num)
                    return count
                else:
                    str+=formula[index]
                index+=1

        fun2(formula,"")
        for i,j in result.items():
            tp={}
            fun(i,tp)
            for a,b in tp.items():
                if a not in ret.keys():
                    ret.setdefault(a, b * j)
                else:
                    ret[a] += b * j
        ret=sorted(ret.items(),key=lambda ret:ret[0])
        # print(ret)
        ret_s=""
        for i in ret:
            i1=i[0]
            i2=i[1]
            if(i2!=1):
                ret_s+=i1+str(i2)
            else:
                ret_s+=i1
        return ret_s



a=Solution()
formula="(((U42Se42Fe10Mc31Rh49Pu49Sb49)49V39Tm50Zr44Og6)33((W2Ga48Tm14Eu46Mt12)23(RuRnMn11)7(Yb15Lu34Ra19CuTb2)47(Md38BhCu48Db15Hf12Ir40)7CdNi21(Db40Zr24Tc27SrBk46Es41DsI37Np9Lu16)46(Zn49Ho19RhClF9Tb30SiCuYb16)15)37(Cr48(Ni31)25(La8Ti17Rn6Ce35)36(Sg42Ts32Ca)37Tl6Nb47Rh32NdGa18Cm10Pt49(Ar37RuSb30Cm32Rf28B39Re7F36In19Zn50)46)38(Rh19Md23No22PoTl35Pd35Hg)41)50"
print(a.countOfAtoms(formula))
