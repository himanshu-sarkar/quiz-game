# Quiz Game

Its's a simple terminal-based quiz game which is built in Python. 10 questions, multiple choice, score tracking, hint system, and a replay option — no libraries except `random`.

Built as my **third Python project** to practice writing and using functions.

---

## What it does

- Asks 10 multiple choice questions (A/B/C/D)
- Shuffles question order every time so it is not the same each run
- Checks each answer and gives instant feedback
- Hint system — type `hint` instead of an answer to get a clue (costs 0.5 points if you get it right)
- Tracks score and lists every question you got wrong at the end
- Shows your score history for the whole session after each round
- Gives honest feedback based on your percentage
- Asks if you want to play again

---

## Functions used in it

| Function | What it does |
|----------|-------------|
| `show_welcome()` | Prints the intro screen |
| `show_score_history()` | Shows all scores from the current session |
| `show_question()` | Displays a single question and its options |
| `check_answer()` | Compares user input with correct answer, returns True/False |
| `get_feedback()` | Takes score and returns a feedback string |
| `show_result()` | Prints final score, percentage, feedback, and wrong questions |
| `play_game()` | Main function that runs the whole game loop |

Each function does exactly one job. That is the whole point.

---

## Sample Output's are

```
=============================================
           QUIZ GAME
=============================================
10 questions. Pick A, B, C or D.
Type 'hint' to get a clue.
Using a hint costs 0.5 points if correct.
=============================================

No previous scores this session.

Enter your name: Himanshu

Alright Himanshu, let us go!

Question 1: Which planet is closest to the sun?
  A) Earth
  B) Venus
  C) Mars
  D) Mercury
  Your answer: hint
  Hint: It is the smallest planet in our solar system.
  Your answer now: D
  Correct!
  (0.5 points — hint was used)

Question 2: What does CPU stand for?
  A) Central Processing Unit
  B) Computer Personal Unit
  C) Central Program Utility
  D) Core Processing Unit
  Your answer: A
  Correct!

...

=============================================
             RESULT
=============================================
Score     : 8.5 / 10
Percentage: 85.0%
Feedback  : Really good. You know your stuff.

Questions you got wrong:
  - Who invented the telephone?
=============================================

--- Your scores this session ---
  Round 1: 8.5 / 10
--------------------------------

Play again? (yes / no): no

Thanks for playing, Himanshu. See you next time.
```

---

## How to run this

```bash
python quiz_game.py
```

No installations needed. Just Python 3.

---

## Things I learned 

- How to define and call functions
- Breaking a program into small single-purpose functions instead of writing everything in one block
- Passing arguments into functions and returning values back
- Using a global list to track data across multiple function calls
- Using `random.shuffle()` to randomize a list
- Adding a hint system with conditional scoring using `if used_hint`
- Calling a function recursively to replay the game

---



---

## Tech stack

- Python 3
- `random` module (built-in, no install needed)
