import random
import string 

st = input("Enter a string: ")
words = st.split(" ")

coding = input("Encode? ")

if(coding.lower() == "y" or coding.lower() == "yes"):
    nwords = []
    for word in words:
        if(len(word)>3):
            r1 = "".join(random.choices(string.ascii_lowercase, k=3))
            r2 = "".join(random.choices(string.ascii_lowercase, k=3))
            # print(r1, r2)
            stNew = r1+word[1:]+word[0]+r2
            nwords.append(stNew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if(len(word)>3):
            stNew = word[3:-3]
            stNew = stNew[-1]+stNew[:-1]
            nwords.append(stNew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
