# ----------------------------------------
# Quiz Game
# A simple terminal quiz with score tracking
# Updated: added hint system, score history, streak bonus, all-time high score
# ----------------------------------------

import random

# This list keeps all scores from this session
# it resets when you close the program (no file saving for session scores)
score_history = []

HIGH_SCORE_FILE = "high_score.txt"

# added a hint key to every question
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C",
        "hint": "It is known as the City of Light."
    },
    {
        "question": "Which planet is closest to the sun?",
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Mercury"],
        "answer": "D",
        "hint": "It is the smallest planet in our solar system."
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Processing Unit", "B) Computer Personal Unit", "C) Central Program Utility", "D) Core Processing Unit"],
        "answer": "A",
        "hint": "It is often called the brain of the computer."
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A) 5", "B) 7", "C) 6", "D) 8"],
        "answer": "C",
        "hint": "Think of the shape of a honeycomb cell."
    },
    {
        "question": "Which language is used for web styling?",
        "options": ["A) Python", "B) CSS", "C) Java", "D) C++"],
        "answer": "B",
        "hint": "It controls colors, fonts, and layouts on websites."
    },
    {
        "question": "What is 12 x 12?",
        "options": ["A) 124", "B) 140", "C) 144", "D) 148"],
        "answer": "C",
        "hint": "It is a perfect square number."
    },
    {
        "question": "Who invented the telephone?",
        "options": ["A) Edison", "B) Tesla", "C) Bell", "D) Newton"],
        "answer": "C",
        "hint": "His first name is Alexander Graham."
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A) 90", "B) 100", "C) 110", "D) 120"],
        "answer": "B",
        "hint": "Same number as centimetres in a metre."
    },
    {
        "question": "Which is the largest ocean?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D",
        "hint": "It covers more than 30% of the Earth's surface."
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A) Random Access Memory", "B) Read Access Module", "C) Run Active Memory", "D) Random Active Mode"],
        "answer": "A",
        "hint": "It is the short term memory your computer uses while running programs."
    }
]


# shows the welcome screen
def show_welcome():
    print("=" * 45)
    print("           QUIZ GAME")
    print("=" * 45)
    print("10 questions. Pick A, B, C or D.")
    print("Type 'hint' to get a clue.")
    print("Using a hint costs 0.5 points if correct.")
    print("Get 3 correct in a row for a 0.5 streak bonus.")
    print("=" * 45)


# shows all the scores from this session
def show_score_history():
    if len(score_history) == 0:
        print("\nNo previous scores this session.")
    else:
        print("\n--- Your scores this session ---")
        for i in range(len(score_history)):
            print(f"  Round {i + 1}: {score_history[i]} / 10")
        print("--------------------------------")


# reads the all-time high score from file, returns 0 if file doesn't exist yet
def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return float(file.read().strip())
    except FileNotFoundError:
        return 0


# writes a new all-time high score to the file
def save_high_score(new_high):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(new_high))


# shows one question with its options
def show_question(number, question_data):
    print(f"\nQuestion {number}: {question_data['question']}")
    for option in question_data["options"]:
        print(f"  {option}")


# checks if the answer is right or wrong
def check_answer(user_answer, correct_answer):
    if user_answer.upper() == correct_answer:
        print("  Correct!")
        return True
    else:
        print(f"  Wrong! The answer was {correct_answer}")
        return False


# returns feedback text based on score percentage
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


# prints the final result screen
def show_result(score, total, wrong_questions, high_score, is_new_high):
    print("\n" + "=" * 45)
    print("             RESULT")
    print("=" * 45)
    print(f"Score     : {score} / {total}")
    print(f"Percentage: {(score / total) * 100:.1f}%")
    print(f"Feedback  : {get_feedback(score, total)}")

    if is_new_high:
        print(f"New all-time high score! ({high_score} / {total})")
    else:
        print(f"All-time high score: {high_score} / {total}")

    if len(wrong_questions) > 0:
        print("\nQuestions you got wrong:")
        for q in wrong_questions:
            print(f"  - {q}")

    print("=" * 45)

    # showing score history after every round
    show_score_history()


# ----------------------------------------
# MAIN GAME
# ----------------------------------------

def play_game():
    show_welcome()
    show_score_history()

    high_score = load_high_score()

    name = input("\nEnter your name: ")
    print(f"\nAlright {name}, let's go!\n")

    random.shuffle(questions)

    score = 0
    streak = 0
    wrong_questions = []
    question_number = 1

    for q in questions:
        show_question(question_number, q)

        used_hint = False
        user_answer = input("  Your answer: ").strip().lower()

        # hint system - if they type hint, show the clue and ask again
        if user_answer == "hint":
            print(f"  Hint: {q['hint']}")
            used_hint = True
            user_answer = input("  Your answer now: ").strip()

        # checking if input is valid
        if user_answer.upper() not in ["A", "B", "C", "D"]:
            print("  Invalid input. Counted as wrong.")
            wrong_questions.append(q["question"])
            streak = 0
        else:
            is_correct = check_answer(user_answer, q["answer"])
            if is_correct:
                if used_hint:
                    print("  (0.5 points — hint was used)")
                    score = score + 0.5
                    streak = 0  # hint use breaks the streak
                else:
                    score = score + 1
                    streak = streak + 1
                    if streak == 3:
                        print("  Streak bonus! +0.5 for 3 in a row")
                        score = score + 0.5
                        streak = 0
            else:
                wrong_questions.append(q["question"])
                streak = 0

        question_number = question_number + 1

    # rounding so it does not show as 8.000000
    final_score = round(score, 1)

    # saving score to history before showing the result
    score_history.append(final_score)

    # check and update all-time high score
    is_new_high = final_score > high_score
    if is_new_high:
        high_score = final_score
        save_high_score(high_score)

    show_result(final_score, len(questions), wrong_questions, high_score, is_new_high)

    again = input("\nPlay again? (yes / no): ").strip().lower()
    if again == "yes":
        play_game()
    else:
        print(f"\nThanks for playing, {name}. See you next time.")


# running the game
play_game()
