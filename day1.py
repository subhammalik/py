#assigment day 1


#factors
# q1=int(input('enter a natural number : '))
# def fac(a):
#     l1=[]
#     for i in range(1,a+1,1):
#         if a%i==0:
#             l1.insert(0,i)
#     return l1
# print(fac(q1))

#calc=====DONE! in day3 assignment

#shuffling cards
# # Python program to shuffle a deck of card using the module random and draw 5 cards
# # import modules
# import itertools, random
# # make a deck of cards
# deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# print(deck)
# # shuffle the cards
# random.shuffle(deck)
# print(deck)
# # draw five cards
# print("You got:")
# for i in range(5):
#    print(deck[i][0], "of", deck[i][1])


#calendar
# import calendar
# w1=int(input('enter year : '))
# w2=int(input('enter month : '))
# print(calendar.month(w1,w2))


#fibonacci using recursion
# w3=int(input('enter a natural number : '))
# def fr(n):
#    if n<=0:
#       return 'enter >0'
#    elif n==1:
#       return 0
#    elif n==2:
#       return 1
#    else:
#       return fr(n-1)+fr(n-2)
#
# print(fr(w3))


#sum of natural numbers using recursion
# w3=int(input('enter a natural number upto which the sum needs to be evaluated : '))
# def sn(n):
#    if n<=0:
#       return 'enter >0'
#    elif n==1:
#       return 1
#    else:
#       return n+sn(n-1)
# print(sn(w3))

#factorial using recursion
# w4=int(input('enter a whole number : '))
# def fac(n):
#    if n<0:
#       return 'enter >=0'
#    elif n==0:
#       return 1
#    else:
#       return n*fac(n-1)
# print(fac(w4))

#decimal to binary using recursion
# w5=int(input('enter a whole number : '))
# def dtb(n):
#    k=[]
#    r=0
#    q=n//2
#    while q!=0:
#       q = n // 2
#       r=n%2
#       k=[r]+k
#       n=q
#    print(k)
#    w6=''.join(str(ww) for ww in k)
#    return w6
# print(dtb(w5))


#add two matrices of order/dimension=3
# def mm():
#    m1=[]
#    m2=[]
#    m3=[[0 for j in range(3)] for i in range(3)]
#    for i in range(3):
#       m2.append([])
#       for j in range(3):
#          k=int(input('enter value: '))
#          m2[i].append(k)
#    for i in range(3):
#       m1.append([])
#       for j in range(3):
#          k=int(input('enter value: '))
#          m1[i].append(k)
#    for i in range(len(m1)):
#       for j in range(len(m1[0])):
#          m3[i][j]=m1[i][j]+m2[i][j]
#    print(m1)
#    print(m2)
#    print(m3)
# mm()


#transpose of a matrix
# def matrans():
#    r1=[]
#    for i in range(3):
#       r1.append([])
#       for j in range(3):
#          k=int(input('enter value : '))
#          r1[i].append(k)
#    print(r1)
#    for i in range(3):
#       for j in range(i,3):
#          if i==j:
#             pass
#          else:
#             r1[i][j]=r1[j][i]
#    print(r1)
# matrans()


#multiply two matrices
# def multmat():
#    r2=[]
#    for i in range(3):
#       r2.append([])
#       for j in range(3):
#          k=int(input('enter value for first : '))
#          r2[i].append(k)
#    r3=[]
#    for i in range(3):
#       r3.append([])
#       for j in range(3):
#          k=int(input('enter value for second : '))
#          r3[i].append(k)
#    print(r2)
#    print(r3)
#    r4=[[0 for j in range(3)] for i in range(3)]
#    for i in range(3):
#       for j in range(3):
#          for k in range(3):
#             r4[i][j] += r2[i][k] * r3[k][j]
#    print(r4)
#
# multmat()


#palindrome
# t1=str(input('enter a single word string or a whole number : '))
# def pal(n):
#    n=n.casefold()
#    nn=reversed(n)
#    if list(nn)==list(n):
#       return True
#    else:
#       return False
# print(pal(t1))


#remove punctuation
# qq=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
# def rp():
#    n=input('enter a string with punctuations(to be removed) : ')
#    nn=list(n)
#    #print(nn)
#    l=[]
#    for i in nn:
#       for j in qq:
#          if i==j:
#             l.append(j)
#    l=''.join(l)
#    print(l)
# rp()


#sort in alphabetical order
# def sa():
#    n=input('enter a string of words/chars to be sorted alphabetically : ')
#    nn=n.split()
#    print(nn)
#    nn.sort()
#    print(nn)
#    nnn=' '.join(nn)
#    print(nnn)
# sa()


#set operations??

#powers of 2 using anonymous function
# y1=int(input('enter a number to be raised : '))
# y2=int(input('enter the power to be raised to : '))
# pow= lambda y,z: y**z
# print(pow(y1,y2))

#divisors/factors==DONE!


# #binary and octal
# w5=int(input('enter a whole number : '))
# def dtb(n):
#    k=[]
#    r=0
#    q=1
#    nn=n
#    while q!=0:
#       q = n // 2
#       r=n%2
#       k=[r]+k
#       n=q
#    w6=''.join(str(ww) for ww in k)
#    k= []
#    r = 0
#    q = 1
#    while q != 0:
#       q = nn //8
#       r = nn % 8
#       k = [r] + k
#       nn= q
#    w7 = ''.join(str(ww) for ww in k)
#    return 'binary',w6,' ','octal',w7
#
# print(dtb(w5))

#armstrong number
# def arm():
#    l=[]
#    n1=int(input('enter starting point of interval(whole number) : '))
#    n2=int(input('enter end point of the interval(whole number) : '))
#    if n1>n2:
#       print('try again! hint:start < end')
#    else:
#       for i in range(n1, n2+1):
#          l.append(i)
#       for j in l:
#          j=int(j)
#          m=j
#          s=0
#          while j!=0:
#             r=j%10
#             q=j//10
#             s+=(r**3)
#             j=q
#          if s==m:
#             print(m,'is an Armstrong number')
#
# arm()


#sum of natural numbers==DONE!











