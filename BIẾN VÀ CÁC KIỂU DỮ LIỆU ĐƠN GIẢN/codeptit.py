from math import *

def snt(u):
    if(u<=1): return False
    for i in range(2, isqrt(u)+1):
        if(u%i==0): return False
    return True

def res(s):
    if(len(s)%2==0): return False
    if(s[0]==s[1]): return False
    tmp = ''
    for i in range(0,len(s),2):
        if(tmp==''): tmp = s[i]
        elif(tmp!=s[i]): return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        if(res(s)): print('YES')
        else: print('NO')

