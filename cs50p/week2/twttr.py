phrase = input("Write the message: ")
answer = ""
for ch in phrase:
    if ch not in "AEIOUaeiou":
        answer += ch
print(answer)