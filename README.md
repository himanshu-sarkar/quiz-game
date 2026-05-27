# Quiz Game 

A simple terminal-based quiz game built in Python. 10 questions, multiple choice, score tracking, and a replay option — no libraries except `random`.

Built as my **third Python project** to practice writing and using functions.

---

## What it does

- Asks 10 multiple choice questions (A/B/C/D)
- Shuffles question order every time so it's not the same each run
- Checks each answer and gives instant feedback
- Tracks score and lists every question you got wrong at the end
- Gives honest feedback based on your percentage
- Asks if you want to play again

---

## Functions used

| Function | What it does |
|----------|-------------|
| `show_welcome()` | Prints the intro screen |
| `show_question()` | Displays a single question and its options |
| `check_answer()` | Compares user input with correct answer, returns True/False |
| `get_feedback()` | Takes score and returns a feedback string |
| `show_result()` | Prints final score, percentage, feedback, and wrong questions |
| `play_game()` | Main function that runs the whole game loop |

Each function does exactly one job. That's the whole point.

---

## Sample Output

```
=============================================
           QUIZ GAME
=============================================
10 questions. Pick A, B, C or D.
Type your answer and press Enter.
=============================================

Enter your name: Himanshu

Alright Himanshu, let's go!

Question 1: Which planet is closest to the sun?
  A) Earth
  B) Venus
  C) Mars
  D) Mercury
  Your answer: D
  ✓ Correct!

Question 2: What does CPU stand for?
  A) Central Processing Unit
  B) Computer Personal Unit
  C) Central Program Utility
  D) Core Processing Unit
  Your answer: B
  ✗ Wrong! The answer was A

...

=============================================
             RESULT
=============================================
Score     : 8 / 10
Percentage: 80.0%
Feedback  : Really good. You know your stuff.

Questions you got wrong:
  - What does CPU stand for?
  - Who invented the telephone?
=============================================

Play again? (yes / no): no

Thanks for playing, Himanshu. See you next time.
```

---

## How to run

```bash
python quiz_game.py
```

No installations needed. Just Python 3.

---

## What I learned

- How to define and call functions
- Breaking a program into small single-purpose functions instead of writing everything in one block
- Passing arguments into functions and returning values back
- Using `random.shuffle()` to randomize a list
- Calling a function recursively to replay the game

---

## What's next

Planning to add:
- Difficulty levels (easy / medium / hard)
- A high score tracker using file handling
- Timer per question

---

## Project progression

| # | Project | Concept |
|---|---------|---------|
| 1 | Calculator | Basics, user input, conditionals |
| 2 | Grade Vault | Loops, nested loops, lists |
| 3 | Quiz Game | Functions, return values, randomization |

---

## Tech stack

- Python 3
- `random` module (built-in, no install needed)
