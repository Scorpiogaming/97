intro=input("enter the string")
cc=0
wc=1
for i in intro:
    cc=cc+1 
    if(i==" "):
        wc=wc+1
print("number of words in string ")
print(wc)
print("number of character in string ")
print(cc)