temp=input("Type an interval: ")
num=int(input("Type an intergal number: "))
i=2
a=0
b=0
temp1=0
while temp1==0:
    if temp[i:i+1]==",":
        a=int(temp[1:i])
        temp1=1
    else:
        i=i+1
j=4
temp1=0
while temp1==0:
    if temp[j:j+1]=="]":
        b=int(temp[i+1:j])
        temp1=1
    else:
     j=j+1
sum1=1
for i in range(a,b+1):
    sum=0
    for j in range(2,b+1): 
        if j!=0:   
            if i%j==0:
                sum=sum+1
    if sum==1:
        sum1=sum1+1
d=[1]*sum1
k=1
for i in range(a,b+1):
    sum=0
    for j in range(2,b+1):
        if j!=0:
            if i%j==0:
                sum=sum+1
    if sum==1:
         d[k]=i
         k=k+1
sum2=1
for i in range (1,sum1):
    for j in range(1,sum1):
        if (-1)*(d[i]-d[j])==num:
            sum2=sum2+2
if sum2==1:
    print ("There is no pair of first number so that d=|p-q|")
else:
    e=[0]*sum2
    k=0
    for i in range(1,sum1):
        sum3=0
        for j in range(1,sum1):
            if (-1)*(d[i]-d[j])==num:
                e[k]=d[i]
                e[k+1]=d[j]
                k=k+2
  
    print ("The first pair of first number in the interval ", temp,"is ",e[0]," and ",e[1])  
