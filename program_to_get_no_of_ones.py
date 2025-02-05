# Program to check number of 1 bits
# using bit maniputaion
num = int(input("Enter a number: "))
cnt = 0
given_num = num
while num!=0:
    if num & 1==1:
        cnt +=1
    num >>=1
print(f"Number of one's in given number:{given_num} are : {cnt}")