 
#Exercise 16: Count Unique Words
str1="vector of hyd or vector of blr and UST"
seen=[]
cnt=0
res=str1.split(" ")
for i in res:
    if i not in seen:
        seen.append(i)
print(seen)
print(len(seen))

print("Count")