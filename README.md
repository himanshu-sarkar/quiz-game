# Quiz Game
Its's a simple terminal-based quiz game which is built in Python. 10 questions, multiple choice, score tracking, hint system, streak bonus, all-time high score, and a replay option — no libraries except `random`.
Built as my **third Python project** to practice writing and using functions.
---
## What it does is
- Asks 10 multiple choice questions (A/B/C/D)
- Shuffles question order every time so it is not the same each run
- Checks each answer and gives instant feedback
- Hint system — type `hint` instead of an answer to get a clue (costs 0.5 points if you get it right, breaks your streak)
- Streak bonus — 3 correct answers in a row (no hints) earns +0.5 bonus points
- Tracks score and lists every question you got wrong at the end
- Shows your score history for the whole session after each round
- Saves your all-time high score to a file so it persists across runs, not just the session
- Gives honest feedback based on your percentage
- Asks if you want to play again
---
## Functions used in this
| Function | What it does |
|----------|-------------|
| `show_welcome()` | Prints the intro screen |
| `show_score_history()` | Shows all scores from the current session |
| `load_high_score()` | Reads the all-time high score from a file (returns 0 if none saved yet) |
| `save_high_score()` | Writes a new all-time high score to the file |
| `show_question()` | Displays a single question and its options |
| `check_answer()` | Compares user input with correct answer, returns True/False |
| `get_feedback()` | Takes score and returns a feedback string |
| `show_result()` | Prints final score, percentage, feedback, wrong questions, and high score status |
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
Get 3 correct in a row for a 0.5 streak bonus.
=============================================
No previous scores this session.
Enter your name: Himanshu
Alright Himanshu, let us go!
Question 1: Which planet is closest to the sun?
  A) Earth
  B) Venus
  C) Mars
  D) Mercury
  Your answer: A
  Correct!
Question 2: What does CPU stand for?
  A) Central Processing Unit
  B) Computer Personal Unit
  C) Central Program Utility
  D) Core Processing Unit
  Your answer: A
  Correct!
Question 3: How many sides does a hexagon have?
  A) 5
  B) 7
  C) 6
  D) 8
  Your answer: C
  Correct!
  Streak bonus! +0.5 for 3 in a row
...
=============================================
             RESULT
=============================================
Score     : 8.5 / 10
Percentage: 85.0%
Feedback  : Really good. You know your stuff.
New all-time high score! (8.5 / 10)
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
No installations needed. Just Python 3. A `high_score.txt` file gets created automatically in the same folder to store your best score.
---
## Things I learned during this project
- How to define and call functions
- Breaking a program into small single-purpose functions instead of writing everything in one block
- Passing arguments into functions and returning values back
- Using a global list to track data across multiple function calls
- Using `random.shuffle()` to randomize a list
- Adding a hint system with conditional scoring using `if used_hint`
- Tracking a streak counter and resetting it on wrong answers or hint use
- Basic file I/O — reading and writing a file with `open()` to persist data across program runs
- Handling a missing file with `try` / `except FileNotFoundError`
- Calling a function recursively to replay the game
---
---
## Tech stack
- Python 3
- `random` module (built-in, no install needed)
- Built-in file I/O (`open()`, no install needed)
