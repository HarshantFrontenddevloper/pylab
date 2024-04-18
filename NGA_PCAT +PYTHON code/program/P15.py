# create  empty  list marks.  keep  adding


marks = []

# while True:
#  x = int(input("Enter the marks , To  stop giving negative marks "))
#  if x>=0 :
#   marks.append(x)
#  else:
#   break



while True:
  x = int(input("Enter the value"))
  if x <= 0:
    break
  marks.append(x)

print(marks)