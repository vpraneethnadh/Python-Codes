def rev(s):
    words = []
    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)
    
    words.reverse()
    return " ".join(words).lower()

input_str = "This is a sentence"
print(rev(input_str))
