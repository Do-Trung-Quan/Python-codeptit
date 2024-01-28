from math import *

'''hướng làm: dùng stack, duyệt qua list input và thêm vào st những phần tử tmdb'''

if __name__ == '__main__':
    n = int(input())
    st = []     #tạo stack rỗng
    a = list(map(int, input().split()))
    for i in a:     #duyệt từng phần tử i của list a
        if(len(st)==0): st.append(i)    #nếu stack rỗng -> push i vào st
        else:
            if((i+st[-1])%2==0):  #nếu st.back() + i là số chắn
                st.pop()    #pop st.back()
            else:
                st.append(i)    #nếu tổng là lẻ -> push i vào st
    print(len(st))  #in ra số phần tử còn lại
