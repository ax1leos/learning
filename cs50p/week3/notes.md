# CS50P Week 3 — Exeptions

## Lecture notes

### Key ideas

- Value Error
- try
- except
- pass

### My explanations (in my own words)

1. Why do we need try?

To stop the program from crashing when an error happens. It lets Python test a block of code safely.

2. What does except ValueError do?

It catches a specific error (like when a user types letters instead of numbers) and runs a backup plan instead of closing the program.

3. Why does while True with try repeat the request?

- while True creates a never-ending loop.
- If the user makes a mistake, the loop starts over to ask again.
- If the input is correct, a break command stops the loop.


## Problems solved

- 
- 

## Breaking get_int

- `abc` → ValueError, программа просит снова.
- Пустая строка → тоже ValueError.
- `3.5` → ValueError, потому что int() не понимает точку.
- `-5` → принимается как -5, потому что int() может быть отрицательным.