# CS50P Week 0 — Functions, Variables

## Lecture notes

### Key ideas

- functions
- arguments
- side effects (can be visual, audio etc.)
- bugs
- variables
- comments
- parameters (e.g. sep, end)
- escape character ( \\ )
- f-string
- name = name.strip() - removes white spaces before and after the string
- name = name.capitalize() - capitalizes the first letter
- name = name.title() - from "john snow" to "John Snow"
- first, last = name.split(" ") - spliting the user's name into first and last name
- print(f"{z:,}") - if z = 1000000 the program will print 1,000,000
- print(f"{z:.2f}") - 2/3 will print 0.67 (2 decimal after the dot)
- scope

### My explanations (in my own words)

1. Why f-strings are useful: They help us to use at the same time variables and strings for a more convenient and understandable output of `print()`
2. What `input()` does and why `int()` is often needed: `input()` always returns a string, even if the user enters a number, so you need to convert it using `int()` or `float()` for math. 
3. Why `if __name__ == "__main__":` is used: if `__name__ == "__main__":` — the code in `main()` runs only when the file is executed directly. When this file is imported into another one, `main()` is not executed.

## Problems solved

- [ ] Indoor Voice
- [ ] Tip Calculator