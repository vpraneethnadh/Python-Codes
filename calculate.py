f=open("student.txt","r")
"""
c=1
big=0
for i in f:
    list=i.split(",")
    marks=int(list[2])

    if c==1:
        small=marks
        big=marks
        c=c+1

    if small>marks:
        small=marks

    if big<marks:
        big=marks
print("LEAST MARKS: ",small)
print("HIGHEST MARKS: ",big)

n=int(input("ENTER ANY NUMBER: "))
for i in f:
    list=i.split(",")

    if n==int(list[0]):
        print("NAME: ",list[1])
        print("MATHS MARKS(100): ",list[2])
        print("PHYSICS MARKS(100): ",list[3])
        print("CHEMISTRY MARKS(100): ",list[4])
        print("TOTAL MARKS(300): ",list[5])
"""

print("sno"+"\t"+"name"+"\t"+"Pass/Fail")
for i in f:
    list=i.split(",")

    sno=int(list[0])
    name=list[1]
    maths=int(list[2])
    physics=int(list[3])
    chemistry=int(list[4])



    if (maths>35) & (physics>35) & (chemistry>35):
        print(str(sno)+"\t"+name+"\t"+"Pass")
    else:
        print(str(sno)+"\t"+name+"\t"+"Fail")

