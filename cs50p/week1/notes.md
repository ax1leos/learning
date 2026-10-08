# CS50P Week 1 — Conditionals

## Lecture notes

### Key ideas

- conditionals
- if, else, elif
- and, or
- match
- .endswith("") в решении задачи File Extensions

### My explanations (in my own words)

1. What is the difference between if and elif? What happens if you write a second if instead of elif? `If` statement will be check anyways, even if the previous conditional was `True`, but `elif` will be checked only if the previous conditional was `False`, so it can save us time, but not in all cases.

2. What do the and, or, not operators do? Give a real-life example. They check the boolean result of the statement: `True` or `False`. Example: Today is Sunday or Saturday, and if even 1 of these is true the return value will be `True`, but example: Today the weather is hot and sunny, only if both statement are true, the return value will be `True`.

3. Why are indents mandatory in Python, and not just "for beauty"? Without them the program will not work, with the help of them we show program which commands related to which conditionals, functions etc.

## Problems solved

- [ ] Math Interpreter
- [ ] Meal Time