Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a//b)
0
print(a/b)
0.5
print(a%b)
2
print(a**b)
16
a=4
b=6
print(a+b)
10
print(a-b)
-2
print(a//b)
0
print(a/b)
0.6666666666666666

print(a%b)
4
print(a**b)
4096
#assignment
a=4
b=6
a+=b
a
10
a-=b
a
4
a*=b
a
24
a//=b
a
4
a/=b
a
0.6666666666666666
a%=b
a
0.6666666666666666
a=2
b=6
a+=b
b
6
#comparision
a=5
b=7
a<b
True
b>a
True
a>b
False
a<=b
True
b>=a
True
a!=b
True
a==b
False
#logical
a=4
b=8
a==b and a!=b
False
a<b and b>a
True
a<=b and b>=a
True
a!=b or a==b
True
a>=b or a<=b
True
not True
False
#identify
a=4.5
if type(a) is float:
    print("true")
else:
    print("false")

    
true
if type(a) is not float:
    print("yes")
... else:
...     print("no")
... 
...     
no
>>> #membership
>>> a=2,4,6,8,10
>>> if 10 in a:
...     print(10)
... 
...     
10
>>> if 8 in a:
...     print(a)
... 
...     
(2, 4, 6, 8, 10)
>>> if 6 in a:
...     print(6)
... 
...     
6
>>> if 20 not in a:
...     print(20)
... 
...     
20
if 10 not in a:
    print(10)

    
