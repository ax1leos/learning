def shorten(text):
    result = ""
    for ch in text:
        if ch not in "AEIOUaeiou":
            result += ch
    return result


def main():
    phrase = input("Write the message: ")
    print(shorten(phrase))


if __name__ == "__main__":
    main()