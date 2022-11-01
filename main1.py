a = int(input('a= '))
b = int(input('b= '))
c = int(input('c='))
Tb1 = 'Không phải PTb2'
Tb2 = 'PTVN'
Tb3 = 'PT có nghiệm kép x ='
Tb4 = 'PT có 2 nghiệm'
if a == 0:
    print(Tb1)
d = b**2-4*a*c
if d<0 :
    print(Tb2)
elif d==0:
    print(Tb3,-b/(2*a))
else:
    print(Tb4,'x1=',(-b+d**0.5)/(2*a), 'x2=',(-b-d**0.5)/(2*a))
