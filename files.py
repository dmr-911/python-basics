# read a file
f = open('myfile.txt', 'r') 
# r for reading file, gives error if file doesn't exists, this is the default pass if no 2nd param is given
# rb for open binary file
# rt for open txt file, this is default
# w for writing files , create new file if file doesn't exists
# a for append files,
# x for create files
text = f.read() # read file
f.close

print(text)

# writing to a file

j = open("myfile.txt", 'w');
j.write("Hello world!")
j.close() #always close after open

# append to a file
k = open("myfile.txt", "a");
k.write("Nice joke.")
k.close() #always close after open

# with open automatically close the file after work
with open("myfile.txt", 'a') as l:
    l.write("Way good way to append....")