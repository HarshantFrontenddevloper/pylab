x=[]
pcnt=0
ncnt=0
psum=0
nsum=0
while True:
 a=int(input("Enter values for a "))
 if a !=0:
    if a >0:
      pcnt=pcnt+1
      psum=psum+a
    if a < 0 :
      ncnt=ncnt+1
      nsum=nsum+a
 else:
   break
print("Pos count  = " , pcnt)
print("Neg count  = " , ncnt)
print("Positive sum = " , psum)
print("Neg sum      = " , nsum)