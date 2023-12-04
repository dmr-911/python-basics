s = {2, 4, 2, 7}
print(s)

s1 = {2, 4, 6}
s2 = {2, 3,5}

print(s1.union(s2))

s1.update(s2)

c1= {"Dk", "DL", "Mi"}
c2 = {"DK", "DT", "DD"}
# print(c1.intersection(c2))
c1.intersection_update(c2)
print(c1)