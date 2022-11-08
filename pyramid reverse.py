row=int(input("Enter the rows"))
p=1 
for i in range(0,row):
    for j in range(0,i+1):
        print(p,end=" ")
        p+=1 
    print()
