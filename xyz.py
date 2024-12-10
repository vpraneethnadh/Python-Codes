
f=open("student.txt","w")

while True:
    stno=input("ENTER STUDENT NUMBER: ")
    if stno=="0":
        break
    else:
        stname=input("ENTER STUDENT NAME: ")
        maths=input("Enter Maths marks: ")
        physics=input("Enter physics marks: ")
        chemistry=input("Enter chemistry marks: ")

        total=int(maths)+int(physics)+int(chemistry)

        f.write(stno+","+stname+","+maths+","+physics+","+chemistry+","+str(total))
        f.write("\n")

f.close()

