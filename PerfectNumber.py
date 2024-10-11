# Perfect Number by using For_loop

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
