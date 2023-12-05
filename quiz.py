print("******************************")
print("welcome to quiz")

question_bank = [
    {"text": " who is hero of vinland saga ..", "answer": "A"},
    {"text": "who is the hero of TWD ..", "answer": "C"},
    {"text": "who is the villian of naruto", "answer": "B"}
]
options = [["A.thorfinn", "B.k", "C.m"],
           ["A.k", "B.p", "C.Rick"],
           ["A.hashi", "B.madara", "C.p"]

           ]
score = 0


def check_answer(user_guess, correct_ans):
    if user_guess == correct_ans:
        return True
    else:
        return False


for question_no in range(len(question_bank)):
    print(question_bank[question_no]["text"])
    for i in options[question_no]:
        print(i)

    guess = input("enter the answer (A/B/C)").upper()
    is_correct = check_answer(guess, question_bank[question_no]["answer"])
    if is_correct:
        print("correct answer")
        score += 1
    else:
        print("incorrect answer")

print(f"your {score}/{len(question_bank)}is")
