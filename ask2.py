num = int(input("Type a positive number: "))
tempp=0
while tempp==0:
    summ=0
    for i in range(2,num+1):
        if num%i==0:    
            summ=summ+1
    if summ==1:
        print ("The number is first and can't be analyzed.")
        num = int(input("Type another positive number or type a negative number to end the program: "))
        if num<0:
            exit(0) 
    else :
        tempp=1
    if num==0:
        print ("The number is zero and can't be analyzed.")
        num = int(input("Type another positive number or type a negative number to end the program: "))
        if num<0:
            exit(0)
        tempp=0
sum3=0
num1=num
b=num**(.5)
for i in range(2,int(b)+1):
    sum2=0    
    for j in range(1,num):
        if i%j==0:
            sum2=sum2+1
    if sum2==2:
        sum3= sum3+1
sum1=0
for i in range(2,num):
    sum=0
    b=num**(.5)
    for j in range(2,int(b)+1):
        if i%j==0:
            sum=sum+1
    if sum==0:
        sum1=sum1+1  
sum4=sum3+sum1+1
c=[1]*sum4
sum3=0
k=1
b=num**(.5)
for i in range(2,int(b)+1):
    sum2=0   
    for j in range(1,int(b)+1):
        if i%j==0:
            sum2=sum2+1
    if sum2==2:
        sum3= sum3+1
        c[k]=i
        k=k+1
sum1=0
for i in range(2,num):
    sum=0
    b=num**(.5)
    for j in range(2,int(b)+1):
        if i%j==0:
            sum=sum+1
    if sum==0:
        sum1=sum1+1
        c[k]=i
        k=k+1
temp=5
sum5=0
while temp==5:
    i=1
    temp1=1
    while temp1==1:
            if num%c[i]==0:
                temp1=2
                num=num/c[i]
                sum5=sum5+1 
            if num==1:
               temp=6  
            i=i+1
sum6=2*sum5+2
d=[1]*sum6
temp=5
sum5=0
j=0
while temp==5:
    i=1
    temp1=1
    while temp1==1:
        if num1%c[i]==0:
            temp1=2
            d[j]=c[i]
            d[j+1]="*"
            j=j+2
            num1=num1/c[i]    
        if num1==1:
            temp=6
        i=i+1
temp10=0
j=0
d[1]=" "
d[sum6-1]=" "
d[sum6-2]=" "
p="The analysis of the number is: "
while temp10==0:
    p =str(p)+str(d[j+1])+str(d[j])
    j=j+2
    if j==sum6:
        temp10=11
print (p)
