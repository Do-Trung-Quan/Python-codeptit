from math import *
def bai1(p,q):
    b = p+q
    c = p*q
    print('x**2 - ', b, '*x + ', c, ' = 0', sep='')

def bai2(n):  #tổng m số lẻ đầu tiên = m^2
    tmp = ceil(n/2)
    print(tmp**2)

def bai3(m,n,a):
    print(m*n*a, 'triệu đồng')

def bai4(a,b,c):
    UCLN = gcd(a,b,c)
    print('UCLN:',UCLN)
    BCNN_ab = a*b // gcd(a,b)
    BCNN = c * BCNN_ab // UCLN
    print('BCNN:', BCNN)

def bai5(r):
    print('CV:', 2*pi*r)
    print('S:', pi*r*r)

def bai6(a,b,c):
    X = -b/(2*a)
    print(a*pow(X,2) + b*X + c)

def bai7(v):
    t = v/9.81
    h = 9.81 * pow(t,2)/2
    d = 331*t
    print(h, d, sep='\n')

def bai8(n,m):
    print(divmod(m,n))

def bai9(n,m):
    leW = (n-1)//3 + 1
    leR = n - leW
    chanR = n//3
    chanW = n - chanR
    W = m//2 * chanW + (m-m//2) * leW
    R = n*m - W
    print(W, R)

def bai10(a1,b1,c1,a2,b2,c2):
    s1 = a1*3600 + b1*60 + c1 - 1
    s2 = a2*3600 + b2*60 + c2
    s = s2 - s1
    gio = s//3600
    phut = (s%3600) // 60
    giay = (s%3600) % 60
    print(gio, 'gio', phut, 'phut', giay, 'giay', sep=' ')

if __name__ == '__main__':
    #bai1:
    # p,q = map(int, input().split())
    # bai1(p,q)

    #bai2:
    # n = int(input())
    # bai2(n)

    #bai3:
    # m,n,a = map(int, input().split())
    # bai3(m,n,a)

    #bai4:
    # a,b,c = map(int, input().split())
    # bai4(a,b,c)

    #bai5:
    # r = float(input())
    # bai5(r)

    #bai6:
    # a,b,c = map(int, input().split())
    # bai6(a,b,c)

    #bai7:
    # v = float(input())
    # bai7(v)

    #bai8:
    # n,m = map(int, input().split())
    # bai8(n,m)

    #bai9:
    # n,m = map(int, input().split())
    # bai9(n,m)

    #bai10:
    a1,b1,c1,a2,b2,c2 = map(int, input().split())
    bai10(a1,b1, c1, a2, b2, c2)
