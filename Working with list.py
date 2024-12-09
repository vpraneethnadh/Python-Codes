Gadgets = ["Mobile","Desktop","Camera","Speakers","Television","Laptop case",100,768.143,22,5555,"Camera lens"]
Words = []
Numbers = []

# (a) Create Separate list for strings and numbers

for i in range(len(Gadgets)):
    temp = Gadgets[i]
    if type(Gadgets[i]) == str:
        Words.append(temp)
    else:
        Numbers.append(temp)

print("Words in the given string are: ",Words)
print("Numbers in the given string are: ",Numbers)

# (b) Sort the strings in Ascending Order

Words.sort()
print("Words in ascending order: ",Words)

# (c) Sort the strings in Descending Order

Words.sort(reverse = True)
print("Words in descending order: ",Words)

# (d) Sort Numbers list from Lowest to Highest

Numbers.sort()
print("Numbers in ascending order: ",Numbers)

# (e) Sort Numbers list from Highest to Lowest

Numbers.sort(reverse = True)
print("Numbers in descending order: ",Numbers)
