class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2


    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)

        return s3

    def __sub__(self,other):
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        s3=student(m1,m2)

        return s3

    def __gt__(self, other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2

        if r1>r2:
            return True
        else:
            return False

    def __mul__(self, other):
        m1=self.m1*other.m1
        m2=self.m2*other.m2
        s3=student(m1,m2)

        return s3

    def __truediv__(self, other):
        m1=self.m1/other.m1
        m2=self.m2/other.m2
        s3=student(m1,m2)

        return s3

    def __floordiv__(self, other):
        m1=self.m1//other.m1
        m2=self.m2//other.m2
        s3=student(m1,m2)

        return s3

    def __mod__(self, other):
        m1=self.m1%other.m1
        m2=self.m2%other.m2
        s3=student(m1,m2)

        return s3

    def __pow__(self, other):
        m1=self.m1**other.m2
        m2=self.m2**other.m2
        s3=student(m1,m2)

        return s3

    def __lt__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2

        if r1 < r2:
            return True
        else:
            return False

s1=student(2,3)
s2=student(50,70)

s3=s1+s2
print("ADDITION",s3.m1)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")



s3=s1-s2
print("SUBSTRACTION:",s3.m1)

s3=s1*s2
print("MULTIPLICATION:",s3.m2)

s3=s1/s2
print("TRUE DIVISION:",s3.m1)

s3=s1//s2
print("FLOAT DIVISION:",s3.m2)

s3=s1%s2
print("MOD:",s3.m1)

s4=student(2,2)
s5=student(3,3)
s3=s4**s5
print("POWER OF:",s3.m1)

if s4<s5:
    print("s4 wins")
else:
    print("s5 wins")
