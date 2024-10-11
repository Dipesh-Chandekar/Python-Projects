#Homework Perfect No, Prime Number, Odd or Even No, Armstrong No, Palindrome 

print("Welcome to My Program to check the Number if it is")

while True:
    print(" 1 -> Perfect Number \n 2 -> Prime Number \n 3 -> Odd Or Even \n 4 -> Armstrong Number \n 5 -> Palindrome \n 0 -> Exit")
    option = int(input("Enter your choice : "))

    if option == 1:
        #Perfect Number
        print("Check the number is Perfect Number or Not")
        x = int(input("Enter the number : "))

        if x <= 1:
            print("Invalid Number")
        else:
            s = 0
            for i in range(1, x):
                if x % i == 0:
                    s += i
            
            if s == x:
                print(f"{x} is a Perfect Number")
            else:
                print(f"{x} is not a Perfect Number")

    elif option == 2:
        #Prime Number
        print("Check the Number is Prime Number or Not")
        x = int(input("Enter a number : "))

        for i in range(2,int(x/2)):
            if(x%i) == 0:
                print(str(x) + " is not prime")
                break
        else:
            print(str(x) + " is prime")

    elif option == 3:
        #Odd Or Even
        print("check if a number is even or odd")
        x = int(input("Enter the number: "))

        if x % 2 == 0:
            print(f"{x} is an Even Number")
        else:
            print(f"{x} is an Odd Number")

    elif option == 4:
        #Armstrong Number
        print("Check whether the given number is armstrong or not")
        n = int(input("Enter a number : "))
        s = n
        b = len(str(n))
        sum1 = 0
        while n != 0:
            r = n % 10
            sum1 = sum1+(r**b)
            n = n//10
        if s == sum1:
            print("The given number", s, "is armstrong number")
        else:
            print("The given number", s, "is not armstrong number")

    elif option == 5:
        #Palindrome
        print("Check if the word or number is Palindrome")
        string = input("Enter a string: ")

        s = string.replace(" ", "").lower()
        is_palindrome = s == s[::-1]

        if is_palindrome:
            print(f"'{string}' is a palindrome")
        else:
            print(f"'{string}' is not a palindrome")

    elif option == 0:
        print("Thanks for using my program")
        break

    else:
        print("Invalid Option")