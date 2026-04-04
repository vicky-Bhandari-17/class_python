src = open("one.txt","r")
data = src.read()
src.close()

dst = open("two.txt","w")
dst.write(data)
dst.close()
print("file copied successfully !")

with open("data.txt","r") as f1, open ("one.txt") as f2, open ("two.txt","w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())
    
print("file copied successfully !")