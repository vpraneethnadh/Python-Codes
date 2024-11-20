#vowels,consonents,words and sentences count
m=input("ENTER ANY PARRAGRAPH: ")
l=len(m)
v=c=w=s=0
for i in range(0,l,1):
    if m[i]=='a' or m[i]=='e' or m[i]=='i' or m[i]=='o' or m[i]=='u':
        v=v+1
    if m[i]!='a' or m[i]!='e' or m[i]!='i' or m[i]!='o' or m[i]!='u':
        c=c+1
    if m[i]==' ':
        w=w+1
    if m[i]=='.':
        s=s+1
print("NUMBER OF VOWELS: ",v)
print("NUMBER OF CONSONUNTS: ",c)
print("NUMBER OF WORDS: ",w+s)
print("NUMBER OF SENTENCES: ",s)