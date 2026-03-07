#1.number of elements:

from array import array
arr= array('i',[10,20,30,40,50])
print(len(arr))

# 2.add element at end:

arr= array('i',[10,20,30])
arr.append(40)
print(arr)

# 3.insert at position:

arr = array('i',[10,20,30])
arr.insert(1,30)
print(arr)

# 4.remove first occurrence:

arr= array('i',[10,20,30,40])
arr.remove(20)
print(arr)

# 5. remove and return last element:

arr=array('i',[10,20,30,40])
x=arr.pop()
print("Removed",x)
print(arr)

# 6. find index of element:

arr=array("i",[10,20,30,40])
print(arr.index(30))

# 7. count occurrences:

arr=array('i',[10,20,30,20,40])
print(arr.count(20))

# 8. reverse array

arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)
