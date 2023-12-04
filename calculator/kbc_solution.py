questions = [
    [
        "Which language was used to create fb?", "Python", "French", "JS", "PHP", "None", 4
    ],
    [
        "Which language was used to create Google?", "Python", "French", "JS", "PHP", "None", 2
    ],
    [
        "Which language was used to create X?", "Python", "French", "JS", "PHP", "None", 1
    ],
    [
        "Which language was used to create Twillio?", "Python", "French", "JS", "PHP", "None", 3
    ],
]

levels = [1000, 10000, 100000, 1000000]

i = 0;
money = 0;

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"Q: {question[0]}")
    print(f"a. {question[1]} b. {question[2]} c. {question[3]} d. {question[4]}")
    reply = int(input("Answer(1 to 4): "))

    if reply == question[-1] :
        money = levels[i]
        print(f"Correct answer , you have won {levels[i]} TK.")

    else :
        print("Wrong answer")
        break;

print(money)