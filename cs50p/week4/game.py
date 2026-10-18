import random

def main():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if int(level) > 0:
                break
        except ValueError:
            pass
        
        
    answer = random.randint(1, int(level))
    
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)        
        except ValueError:
            continue
        if guess < 1:
            continue
        if guess == answer:
            return print("Just right!")
        elif guess < answer:
            print("Too small")
        elif guess > answer:
            print("Too large")        
    
main()