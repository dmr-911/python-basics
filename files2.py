# read lines method
f = open("myfile.txt", 'r')

while True:
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Mark of student 1 is {m1*2}")
    print(f"Mark of student 2 is {m2*2}")
    print(f"Mark of student 3 is {m3*2}")

# write lines method
lines = ["Line 1", "Line 2", "Line 3"]
j = open("myfile2.txt", "w");
# j.writelines(lines)
for line in lines:
    j.write(line + "\n")
j.close()