num=(input("enter the num:"))
k=1
sum=0
for i in range(0,len(num)):
    k=k*int(num[i])
    sum=sum+k
print(sum)
