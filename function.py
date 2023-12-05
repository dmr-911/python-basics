
def average(*numbers):
    ''' numbers is arguments which python converts in a tuple '''
    sum = 0;
    for n in numbers :
        sum = sum + n
    print("average is :", sum / len(numbers))
average(7,2, 3, 4)

def name(**name):
    ''' numbers is arguments which python converts in a dictionary, key:value pair '''
    print(name["mname"],name["fname"])

name(mname="Hello", fname="Mizan")