# CS50P Week 2 — Loops and Data Structures

## Lecture notes

### Key ideas

- while
- for
- list
- len
- dict
- nested loops

### My explanations (in my own words)

1. When is while more convenient, and when is for?

 `for` — when you know what you're iterating over: a list, a string, a range, a file. You go through elements one by one. `while` — when you repeat until some condition changes, and you don't know in advance how many iterations it'll take.

2. What is the difference between list and dict? In which cases should each be used?

 `list` — an ordered collection, accessed by position (index 0, 1, 2, ...).Use when: order matters, you have duplicates, you iterate through everything, you access by position. `dict` — a collection of key → value pairs, accessed by key (usually a string or number). Use when: you look things up by name/id, you want fast lookup by key, order isn't the point (though Python 3.7+ preserves insertion order).

3. What do break and continue do? How do they differ?

Both only work inside a loop. `break` — stop the loop entirely, jump out. `continue` — skip the rest of this iteration, go to the next one.



## Problems solved

- [ ] camelCase
- [ ] Just setting up my twttr