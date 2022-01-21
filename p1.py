n=int(input("Enter number: "))
sum=0
s=0
while(n!=0):
    mod=n%10
    x=mod%2
    if(x==0):
        sum+=mod
    else:
        s+=mod
    n=n//10
print(sum,s)

