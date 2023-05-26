import sys

args = sys.argv



n = int(args[1])

if(n >= 1000):
    print("1000以上は判定できません",end="")

else:

    def primefactor(n):
        ar = []
        temp = n
        for i in range(2, int(n ** 0.5) + 1):
            while temp % i == 0:
                temp //= i
                ar.append(i)

        if temp != 1:
            ar.append(temp)

        if ar == []:
            ar.append(n)

        return ar

    result = primefactor(int(n)) 

    if(len(result) == 1) and (result[0] != 1):
        print("prime",end="")

    else:
        print("not",end="")
