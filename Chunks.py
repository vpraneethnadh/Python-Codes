def chunks(lst,n):
    chunks = []
    for i in range(0, len(lst), n):
        chunks.append(lst[i:i + n])

    print(chunks)

lst = [1,2,3,4,5,6,7,8,9,10]
n = 3
chunks(lst,n)