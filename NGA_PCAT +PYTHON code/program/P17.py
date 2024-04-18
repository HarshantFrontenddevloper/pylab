# # Print characters from a string that are present at an even index number

# name = "harsh kumar "

# # print(name[::2])



# # list1="Harsh kumar"
# # name2 = [x for ind, x in enumerate(name) if ind%2==0]
# # print(name2)


# # for i in range(0, len(string), 2):
# #  print(string[i], end=" ")




# # name = input("Enter String ")
 
# # even_char = ""
# # for i in range(len(name)):
# #     if i % 2 == 0:
# #         even_char += name[i]
 
# # print("Characters at even index:", even_char)

name=input("Enter string  ")

a=len(name)

i=0

while i<a:

    if i%2==0:

      print(name[i])

      i=i+1

    else:

      i=i+1