
l = [3,5,6,7,8,1, 9,0]

print(l[-1]); # negative index
print(l[1:-1])
print(l[1:4])
print(l[::2]) #jump statement, jump 2
print(l[:]) # first statement is starting index (if not declared is 0), second is (len-1) if not declared


# List comprehension
lst = [i*i for i in range(4)]
print(lst)
lst2 = [i*i for i in range(10) if i%2 == 0]
print(lst2)

# Longer version of comprehension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Shorter version of comprehension
newlist2 = [x for x in fruits if "a" in x]
print(newlist2)


l = [0,1,2,3]
m = l
m[0] = 2
print(l);

newlist2.extend(l)
print(newlist2)