#code1
n1=(3.22,11,False,'A-team')
print(n1)
print(n1[1])
print(n1[0])
print(n1[:3])
print(n1[-3:])
print(n1[1:3])


#code2
n2=('Bohr','Leibniz','Einstein')
n3=[]
n4=[9,8,7,6,5,4,3,2,1,0]
for i in n2:
    print(i)
for i in range(int(len(n4)/2)-3,int(len(n4)/2)+3):
    n3.append(n4[i])
print(n3)






