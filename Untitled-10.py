import re
f=input("ENTER FILE NAME: ")
if len(f)<1:f="chapter10.txt"
handle=open(f)
lst=list()
for line in handle :
    y=re.findall('[0-9]+',line)
    lst=lst+y

sum=0
for z in lst :
    sum=sum+int(z)

print (sum)
    