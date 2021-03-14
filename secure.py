print("MESSAGE SENDER")
print("Hello MIT Cell")
k=int(input("Please enter k value to shift transform message: "))
message=input("Now please type your message: ")
list=[]
for i in message:
    if i==" ":
        list.append("@")
    elif i==".":
        list.append("#")
    elif i.isalnum()==True:
      o=ord(i)+k
      a=chr(o)
      if i.isdigit()==True and a.isdigit()==False :
          k2=o-57
          list.append(chr(47+k2))
      elif i.isupper()==True and a.isupper()==False:
          k2=o-90
          list.append(chr(64+k2))
      elif i.islower()==True and a.islower()==False:
          k2=o-122
          list.append(chr(96+k2))
      else:
          list.append(a)
    else:
        list.append(i)
print("You send- ",end="")
for i in list:
    print(i,end="")
print()
print()
print("MESSAGE RECEIVER")
print("Hello Instructor: ")
print("You got a message: ",end="")
for i in list:
    print(i,end="")
print()
decrypted=int(input("To read this in original please type k value provided by cell:- "))
if decrypted==k:
    print("Original Message: ",message)
else:
    print("You are not allowed to read the message!")
