# seek and tell function
# seek
with open("myfile2.txt", "r") as f:
    # move to the 10th byte in the file
    f.seek(10)

    # read the next 5 bytes
    j = f.read(5) # read also takes bytes as parameter
    print(j)
    # tell method tells you which byte we are in, 
    # for this func we are in 10 + 5 bytes ahead, result will be 16
    print(f.tell())

    # we declared that our file does not contain more than 5 bytes
    f.truncate(5) 