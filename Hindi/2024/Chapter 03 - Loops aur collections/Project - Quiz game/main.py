# Basic quiz game

import random

questions = [
    {
        "question": "Ordered sequence me items store karne ke liye kaunsa data type use hota hai?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "correct_answer": "List",
    },
    {
        "question": 'Python seekhne ka sabse practical tareeka kya hai?',
        "options": [
            "Python docs ko word-by-word yaad karna",
            "Internet se code copy-paste karna bina samjhe",
            "Practice karna aur mistakes se seekhna",
            "Code ko kabhi run hi na karna",
        ],
        "correct_answer": "Practice karna aur mistakes se seekhna",
    },
    {
        "question": "Key ke saath value store karne ke liye kaunsi Python collection use hoti hai?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "correct_answer": "Dictionary",
    },
    {
        "question": "Apna code test karne ke liye best jagah kaunsi hai?",
        "options": [
            "Seedha production me",
            "Controlled test environment me",
            "Test ki zarurat nahi; Python chup hai to sab theek hai",
            "Dost ke computer par, taki blame bhi udhar jaye",
        ],
        "correct_answer": "Controlled test environment me",
    },
    {
        "question": "Ek word ke har character par chalne ke liye kaunsi structure use karni chahiye?",
        "options": ["for loop", "while loop", "if statement", "print statement"],
        "correct_answer": "for loop",
    },
    {
        "question": "Python me duplicates avoid karne ke liye kaunsi collection helpful hai?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "correct_answer": "Set",
    },
    {
        "question": "Loop me enumerate() ka common use kya hai?",
        "options": [
            "Item ke saath index bhi lena",
            "List ko delete karna",
            "String ko integer banana",
            "Program ko band karna",
        ],
        "correct_answer": "Item ke saath index bhi lena",
    },
]

score = 0
answered_questions = 0

print("Basic quiz game me aapka swagat hai!")
print("Har sawal ke liye 1-4 enter karo. Bahar nikalne ke liye q enter karo.")

random.shuffle(questions)

for index, question in enumerate(questions, start=1):
    print(f"\n{index}/{len(questions)}: {question['question']}")

    for option_number, option in enumerate(question["options"], start=1):
        print(f"{option_number}. {option}")

    user_answer = input("Aapka jawab (1-4 ya q): ").strip().lower()

    if user_answer == "q":
        print("Quiz se bahar nikal rahe hain.")
        break

    answered_questions += 1

    if (
        user_answer.isdigit()
        and 1 <= int(user_answer) <= len(question["options"])
        and question["options"][int(user_answer) - 1] == question["correct_answer"]
    ):
        print("Sahi! Aapko ek point mila.")
        score += 1
    else:
        print(f"Galat. Sahi jawab hai: {question['correct_answer']}")

print(f"\nGame khatam. Aapka final score: {score}/{answered_questions}")
