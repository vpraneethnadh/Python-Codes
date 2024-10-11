n = input("Enter your Blood group: ")

if n == "o+" or "O+":
    print("Suitable Blood groups are: O+,O-")
elif n == "o-" or "O-":
    print("Suitable Blood groups is: O-")
elif n == "a+" or "A+":
    print("Suitable Blood groups are: O+,O-,A+,A-")
elif n == "a-" or "A-":
    print("Suitable Blood groups are: O-,A-")
elif n == "b+" or "B+":
    print("Suitable Blood groups are: O+,O-,B+,B-")
elif n == "b-" or "B-":
    print("Suitable Blood groups are: O-,B-")
elif n == "AB+" or "ab+":
    print("Suitable Blood groups are: O+,O-,A+,A-,B+,B-,AB+,AB-")
elif n == "AB-" or "ab-":
    print("Suitable Blood groups are: O-,A-,B-,AB-")
else:
    print("Enter a valid Blood Group...")