# [3:45 PM] N Murugadoss
marks=[]

print(type(marks))

print(len(marks))

for i in range(5):
    x=int(input("Enter value for marks  "))
    marks.append(x)

print(marks)

print("maximum marks  " , max(marks))

print("minimum marks  " , min(marks))

print("Total marks    " , sum(marks))
print("Total average    " , sum(marks)/len(marks)+1)