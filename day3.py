##assignment3


#1 fibonacci
# def fib(n):
#     if n==0:
#         return 'enter > 0'
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(10))


#2 sum of 2
# def sum(a,b):
#     return a+b
#
# print(sum(3,4))

#3 menu based calculator
# print('menu calc...')
# n1=int(input('enter the operation type as (sum,diff,prod,div,mod: 1,2,3,4,5) : '))
# n2=float(input('enter the first number : '))
# n3=float(input('enter the second number : '))
# def cal(a,b,c):
#     if c==1:
#         return a+b
#     elif c==2:
#         return a-b
#     elif c==3:
#         return a*b
#     elif c==4:
#         return a/b
#     else:
#         return int(a)%int(b)
# print(cal(n2,n3,n1))


#4 function based calc
# print('func calc...')
# m1=input('what you want to calculate, use a " " for separation : ')
# l=m1.split(" ")
# m2=float(l[0])
# m3=l[1]
# m4=float(l[2])
# def calf(a,b,c):
#     if c=='+':
#         return a+b
#     elif c=='-':
#         return a-b
#     elif c=='*':
#         return a*b
#     elif c=='/':
#         return a/b
#     else:
#         return int(a)%int(b)
# print(calf(m2,m4,m3))

#5 max of 2
# a1=input(" enter the 2 numbers to compare separated by ' ' : ")
# a2=a1.split(" ")
# a3=float(a2[0])
# a4=float(a2[1])
# def max(a,b):
#     if a>b:
#         return a,'is greater'
#     elif a<b:
#         return b,'is greater'
#     else:
#         return 'both are equal'
# print(max(a3,a4))

#6 max of 3
# a1=input(" enter the 3 numbers to compare separated by ' ' : ")
# a2=a1.split(" ")
# a3=float(a2[0])
# a4=float(a2[1])
# a5=float(a2[2])
# def max3(a,b,c):
#     if a>b:
#         if a>c:
#             return a,'is greatest'
#         elif a<c:
#             return c,'is greatest'
#         else:
#             return a,c,'are equal and greatest'
#     elif a<b:
#         if b>c:
#             return b,'is greatest'
#         elif b<c:
#             return c,'is greatest'
#         else:
#             return b,c,'are equal and greatest'
#     else:
#         if a>c:
#             return a,b,'are equal and greatest'
#         else:
#             return c,'is greatest'
# print(max3(a3,a4,a5))

#7 length
# o1 = input('enter a string of characters ')
# o2 = o1.split(' ')
# print(o2)
# def leng(ll):
#     m = 0
#     for i in ll:
#         m += 1
#     return m
# print(leng(o2))


#8 vowel
# q1=input('enter a character ')
# def vow(str):
#     lis=('a', 'A', 'I', 'i', 'O', 'o', 'E', 'e', 'U', 'u')
#     for i in lis:
#         if i==str:
#             return True
#     else:
#         return False
#
# print(vow(q1))


#9 robber's lang
# q2=input('enter a sentence ')
# def trans(a):
#
#     lis = ('a', 'A', 'I', 'i', 'O', 'o', 'E', 'e', 'U', 'u',' ')
#     l1=list(a)
#     l2=[]
#     print(l1)
#     for i in l1:
#         c=0
#         for j in lis:
#             if i==j:
#                 c+=1
#         if c==0:
#             i=i+'o'+i
#         l2.append(i)
#         l3=''.join(l2)
#     print(l3)
# trans(q2)


#10 sum_mul
# w1=input("enter a set of numbers, separated by ' ' : ")
# w2=w1.split(' ')
# print(w2)
# def sumul(a):
#     s1=0.0
#     s2=1.0
#     for i in a:
#         i=float(i)
#         s1+=i
#         s2*=i
#     return 'sum',s1,'prod',s2
# print(sumul(w2))



#11 rev
# r1=input("enter a sentence : ")
# r2=list(r1)
# def re(a):
#     r3=[]
#     for i in r2:
#         r3.insert(0,i)
#     r4=''.join(r3)
#     return r4
#
# print(re(r2))






