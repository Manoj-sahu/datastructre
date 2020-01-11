# GCD - greatest common divisor - given 2 no, start from 1 and check which is the highest no is dividing the both

def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a
    # if a == b:
    #     return a
    # elif  a%b == 0:
    #     return b
    # elif b%a == 0:
    #     return a
    # elif a<b:
    #     return gcd(a%b, b)
    # else:
    #     return gcd(b%a, a)

print(gcd(6, 8))