kbc = [
    {
        "qs" : "How are you? ",
        "ans" : "Fine"
    },
    {
        "qs" : "How old are you? ",
        "ans" : "10"
    },
    {
        "qs" : "How are you feeling? ",
        "ans" : "Fine"
    },
    {
        "qs" : "what are you doing? ",
        "ans" : "code"
    },
]

for set in kbc:
    qs = input(set["qs"])
    if(qs.lower() != set["ans"].lower()):
        print("You lost!")
        break;
    if(kbc.index(set) == len(kbc) - 1):
        print("You are a crorepati!")