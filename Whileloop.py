# (1) print numbers from 1 to 10.

i=1
while i<= 10:
    print(i)
    i=i+1
    
# (2) su of first n nutural numbers:

n=int(input("Enter n:"))
i=1 
s=0
while i<=n:
    s=s+i
    i=i+1
    print("sum=",s)

# (3) table of a numbers:
num=int(input("Enter number:"))
i=1
while i<=10:
    print(num,"x","i","=",num*i)