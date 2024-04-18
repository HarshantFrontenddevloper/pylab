staff=["Vaibhav" , 22 , 74.67 , False]
print(type(staff))
print("No of elements  = " , len(staff))
print("First element   = " , staff[0])
print("First element   = " , staff[-4])
 
print(staff)
 
for i in staff:
    print(i, end=" ")

staff[1]=23    # possible because list is mutable , can be modified
print(staff)
 