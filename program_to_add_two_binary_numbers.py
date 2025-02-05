# Program to add two binary numbers

n1=input("Enter number1: ")
n2=input("Enter number2: ")
tmp = 0
if len(n1)>len(n2):
    tmp = len(n1)-len(n2)
    n2 = tmp*'0' +n2
else:
    tmp = len(n2)-len(n1)
    n1 = tmp*'0'+n1
sume = ''
i=len(n1)-1
coeff = 0
while i>=0:
    rem = str((coeff + int(n1[i]) + int(n2[i])) %2)
    coeff = (coeff +int(n1[i]) + int(n2[i]) ) //2
    sume = rem + sume
    i -=1
if coeff:
    sume = str(coeff) + sume
print(f"the result of binary add: {sume}")


