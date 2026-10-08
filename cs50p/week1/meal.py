def main():
    time = input("What time is it? ")
    new_time = convert(time)
    if 7 <= new_time <= 8:
        print("breakfast time")
    elif 12 <= new_time <= 13:
        print("lunch time")
    elif 18 <= new_time <= 19:
        print("dinner time")


def convert(time_input):
    hour, minutes = time_input.split(":")
    return int(hour) + (int(minutes) / 60)


if __name__ == "__main__":
    main()