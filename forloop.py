# (1) print numbers form 1to5
for i in range (1,6):
   print(i)
   
# (2) print a message 3 times.
for i in range (3):
    print("HELLO")
    
# (3) print Numbers form 1to10.
for i in range (1 ,11):
    print(i)
    
# (4) print Even Numbers form 1to20.
for i in range (1 ,21):
      if i % 2 == 0:
       print(i)
       
# (5) print odd Numbers form 1to15.
for i in range (1 ,16):
      if i % 2 != 0:
       print(i)
       
# (6) print Table of 5.
for i in range (1 ,11):
      print("5x",i,"=",5*i)
       
# (7) print Charactera of a string.
name="Vicky"
for letter in name:
   print(letter)
   
# (8) Sum of Numbers from 1to5.
total =0
for i in range (1,6):
   total=total+i
   print("sum is :",total)
   
# (9) print list Elements.
numbers=[10,20,30,40]
for n in numbers:
   print(n)