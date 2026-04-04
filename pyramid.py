n= int(input("enter number of lines:"))
for i in range(1 , n+1):
    print("*" * 1)
    
for i in range (1 ,4):
    print("*" * i)

n = 5
for i in range(1 , n+1):
    for j in range (1 ,i +1):
        print(j,end="")
        print()
        
n = int(input("enter number of lines:"))
i = 1
while i <= n:
    print("*" * 1)
    i+=1
    
n = int(input("enter number of lines:"))
i = n
while i >= 1:
    print("*" * i)
    i -= 1
    
