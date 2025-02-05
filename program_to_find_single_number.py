# Program to find the singe number 
# Used bit maniputaion concept
data = [2,1,3,1,3,2,8,9,9]
single_number=0
for i in data:
    single_number ^=i
print(f"Single numebr is {single_number}")