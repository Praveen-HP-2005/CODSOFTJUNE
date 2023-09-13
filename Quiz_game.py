import random

questions = [
    {
        "question": "At which year was Formula one's first race held?",
        "options": ["1950", "1948", "1962", "1974"],
        "correct_answer": "1950",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
    },
    {
        "question": "Which football team won the World Cup in the year 2023",
        "options": ["Paris", "India", "Argentina", "Peru"],
        "correct_answer": "Argentina",
    },
    {
        "question": "Which cricket team won world cup in the year 2011",
        "options": ["India", "Sri Lanka", "New Zealand", "Australia"],
        "correct_answer": "India",
    },
    {
        "question": "What is the satellite name that landed on moon's south pole?",
        "options": ["Chandrayaan-2", "Chandrayaan-3", "Aditya-l1", "Sputnik 1"],
        "correct_answer": "Chandrayaan-3",
    },
]

# To shuffle the questions
random.shuffle(questions)

# Initialize the score
score = 0

# Welcome message and rules
print("Welcome to the Quiz Game!")
print("You will be asked multiple-choice questions. Choose the correct option.")
print("Let's get started!\n")

# Quiz loop
for index, question_data in enumerate(questions, 1):
    print(f"Question {index}: {question_data['question']}")

    # To display options
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")

    # Get user's input
    user_answer = input("Enter the number of your answer: ")

    # To check if the answer is correct
    correct_answer = question_data["correct_answer"]
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if 1 <= user_answer <= len(question_data["options"]):
            user_choice = question_data["options"][user_answer - 1]
            if user_choice == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Sorry, the correct answer is: {correct_answer}")
        else:
            print("Invalid choice. Please choose a valid option.")
    else:
        print("Invalid input. Please enter a number.")

# Display final score
print("\nQuiz completed!")
print(f"Your final score is: {score}/{len(questions)}")

if score == len(questions):
    print("Congratulations! You got a perfect score!")
elif score >= len(questions) // 2:
    print("Well done! You did a good job.")
else:
    print("Keep practicing. You can do better next time!")

