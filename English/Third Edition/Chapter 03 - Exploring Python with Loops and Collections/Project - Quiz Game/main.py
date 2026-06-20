# Define the list of questions and answers
import random

questions = [
    {
        "question": "Who was buried in Andrew Jackson grave?",
        "options": ["Donald Trump", "Andrew Jackson", "John Tyler", "Joe Biden"],
        "correct_answer": "Andrew Jackson",
    },
    {
        "question": "What color was George Washington’s great white horse?",
        "options": ["Black", "Brown", "White", "Green"],
        "correct_answer": "White",
    },
    {
        "question": "What data type is used to store items as a sequence that "
                    "can maintain order?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "correct_answer": "List",
    },
    {
        "question": "To loop over each character in a word, which Python "
                    "structure should you use?",
        "options": ["For loop", "While loop", "If statement", "Print Statement"],
        "correct_answer": "For loop",
    },
    {
        "question": "Which Python collection allows us to store unique items "
                    "identified by a key?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "correct_answer": "Dictionary",
    },
    {
        "question": "Which Python collection type prevents duplicates?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "correct_answer": "Set",
    }
]

# Initialize the user's score
score = 0

# Welcome message
print("Welcome to the Basic Quiz Game!")

# Main game loop
random.shuffle(questions)
for i, question in enumerate(questions):

    # Display the list of questions
    print(f"{i+1}/{len(questions)}: {question['question']}")

    # Display the options
    for o, option in enumerate(question['options']):
        print(f"{o+1}. {option}")

    user_answer = input("Your answer (1-4): ")

    # Check if the user's answer is correct
    if (
        user_answer.isdigit()
        and 1 <= int(user_answer) <= len(question['options'])
        and question['options'][int(user_answer) - 1] == question['correct_answer']
    ):
        print("Correct! You earned a point.")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {question['correct_answer']}")

# Game over
print(f"\nGame over! Your score is: {score}/{len(questions)}")
