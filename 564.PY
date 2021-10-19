a = input()
if  len(a) == 3:
    a == int(a)
print(f' {a//100 + a%100//10 + a%10}, {a//100 * a%100//10 * a%10}')



import math
def circle(x, y, r, _x, _y):
    return (x-_x)**2 + (y-_y)**2 <= r**2

x, y = 0, 0
_x = int(input())
_y = int(input())    
r = int(input())

print(circle(x, y, r, _x, _y))



def string_check (str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False

string_check("djg", "gjd"), string_check("tre", "tyu")


a = input()
b = a.split(',')
c = list(map)(int, b)
print(b)


array = [1, 3, 4, 2]
[i*i for i in array]


def sort_abs(lst):
    lst.sort(key = lambda x:abs(x), reverse = True)
    return lst

lst = [1, 3, 4, 2]
sort_abs(lst)



import re 
from math import sqrt
def dicrimin (string):
    check = r'[0-9]*[^\*x+=]'
    lst = list(map(lambda x: int(x), re.findall(check, string)))
    dis = lst[1]**2 - 4*lst[0]*lst[2]
    if dis > 0:
        return ((lst[1]*(-1) + sqrt(dis)/2/lst[0]), (lst[1]*(-1) - sqrt(dis)/2/lst[0]))
    
    if dis == 0:
        return (lst[1]*(-1)/2/lst[0])

    if dis < 0:
        return None

dicrimin("12*x*x+34*x+7=0")


def fact(a):
    if a<=1:
        return 1
    return (a*fact(a-1))


def is_prime(n): 
    d = 2
    while (d*d <= n and n%d != 0):
        d += 1
    return (d*d < n)     


a = 987
b = 343

a, b = b, a


12 14 15 на дом на оценку 