import json
with open("question.json","r") as file:
    data=json.load(file)
score=0
for q in data:
    print("Question :",q["question"])
    for i,opt in q["options"].items():
        print(f"{i}.{opt}")
    user_input=input()
    if user_input==q["answer"]:
        score=score+1
    else:
        print("correct",q["answer"])
print("score",score)
print("Quiz Ends")