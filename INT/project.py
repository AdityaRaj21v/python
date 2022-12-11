a=input("Enter Start Date: ").split("/")
b=input("Enter End Date: ").split("/")
leap=[]
n_leap=[]
for i in range(int(a[-1]),int(b[-1])+1):
    if i%4==0:
        leap.append(i)
    
    else:
        n_leap.append(i)
print("\n")

print("Leap Years Are:")

print("\n")

print(*leap,sep=",")

print("\n")

print("Non Leap Years Are:")

print("\n")

print(*n_leap,sep=",")



