# Prime Number

print("Check the Number is Prime Number or Not")
x = int(input("Enter a number : "))

for i in range(2,int(x/2)):
    if(x%i) == 0:
        print(str(x) + " is not prime")
        break
else:
    print(str(x) + " is prime")
