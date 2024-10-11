def buzz_game(f, t, num):
    num_str = str(num)
    for i in range(f, t):
        contain = False
        for digit in str(i):
            if digit == num_str:
                contain = True
                break

        if i % num == 0 or contain:
            print("Buzz", end=", ")
        else:
            print(i, end=", ")

def main():
    print("Buzz Game")
    print("Define the range")
    f = int(input("Enter the number from: "))
    t = int(input("Enter the number to: "))
    num = int(input("Which number you want to buzz: "))
    buzz_game(f, t, num)

if __name__ == "__main__":
    main()