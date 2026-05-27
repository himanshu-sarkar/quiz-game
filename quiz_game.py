# ----------------------------------------
# Quiz Game
# A simple terminal quiz with score tracking
# ----------------------------------------

import random

# all questions stored as a list of dictionaries
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is closest to the sun?",
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Mercury"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Processing Unit", "B) Computer Personal Unit", "C) Central Program Utility", "D) Core Processing Unit"],
        "answer": "A"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A) 5", "B) 7", "C) 6", "D) 8"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web styling?",
        "options": ["A) Python", "B) CSS", "C) Java", "D) C++"],
        "answer": "B"
    },
    {
        "question": "What is 12 x 12?",
        "options": ["A) 124", "B) 140", "C) 144", "D) 148"],
        "answer": "C"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["A) Edison", "B) Tesla", "C) Bell", "D) Newton"],
        "answer": "C"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A) 90", "B) 100", "C) 110", "D) 120"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A) Random Access Memory", "B) Read Access Module", "C) Run Active Memory", "D) Random Active Mode"],
        "answer": "A"
    }
]


# this function just shows the welcome screen
def show_welcome():
    print("=" * 45)
    print("           QUIZ GAME")
    print("=" * 45)
    print("10 questions. Pick A, B, C or D.")
    print("Type your answer and press Enter.")
    print("=" * 45)


# this function shows one question and its options
def show_question(number, question_data):
    print(f"\nQuestion {number}: {question_data['question']}")
    for option in question_data["options"]:
        print(f"  {option}")


# this function takes the user's answer and checks it
def check_answer(user_answer, correct_answer):
    if user_answer.upper() == correct_answer:
        print("  ✓ Correct!")
        return True
    else:
        print(f"  ✗ Wrong! The answer was {correct_answer}")
        return False


# this function takes the score and returns feedback
def get_feedback(score, total):
    percentage = (score / total) * 100

    if percentage == 100:
        feedback = "Perfect score! Genuinely impressive."
    elif percentage >= 80:
        feedback = "Really good. You know your stuff."
    elif percentage >= 60:
        feedback = "Decent. Some gaps but mostly solid."
    elif percentage >= 40:
        feedback = "Below average. Go back and revise."
    else:
        feedback = "Rough. A lot to work on."

    return feedback


# this function shows the final result
def show_result(score, total, wrong_questions):
    print("\n" + "=" * 45)
    print("             RESULT")
    print("=" * 45)
    print(f"Score     : {score} / {total}")
    print(f"Percentage: {(score / total) * 100:.1f}%")
    print(f"Feedback  : {get_feedback(score, total)}")

    if len(wrong_questions) > 0:
        print("\nQuestions you got wrong:")
        for q in wrong_questions:
            print(f"  - {q}")

    print("=" * 45)


# ----------------------------------------
# MAIN GAME - this is where it all runs
# ----------------------------------------

def play_game():
    show_welcome()

    name = input("\nEnter your name: ")
    print(f"\nAlright {name}, let's go!\n")

    # shuffling so questions come in random order each time
    random.shuffle(questions)

    score = 0
    wrong_questions = []
    question_number = 1

    for q in questions:
        show_question(question_number, q)

        user_answer = input("  Your answer: ").strip()

        # basic input check - if they type something weird, mark it wrong
        if user_answer.upper() not in ["A", "B", "C", "D"]:
            print("  Invalid input. Counted as wrong.")
            wrong_questions.append(q["question"])
        else:
            is_correct = check_answer(user_answer, q["answer"])
            if is_correct:
                score = score + 1
            else:
                wrong_questions.append(q["question"])

        question_number = question_number + 1

    show_result(score, len(questions), wrong_questions)

    # asking if they want to play again
    again = input("\nPlay again? (yes / no): ").strip().lower()
    if again == "yes":
        play_game()
    else:
        print(f"\nThanks for playing, {name}. See you next time.")


# running the game
play_game()
