a = int(input())
b = int(input())
c = int(input())
if a == 0 :
    print('Đây không phải PT bậc 2')
d = b**2 - 4*a*c
if d<0:
    print('PTVN')
elif d == 0:
    print('PT có nghiệm kép',-b/(2*a))
else:
    print('PT có 2 nghiệm x1=', (-b+d**0.5)/(2*a), 'x2=',(-b-d**0.5)/(2*a)) 