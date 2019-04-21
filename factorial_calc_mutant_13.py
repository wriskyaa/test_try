# Python program to find the factorial of a number provided by the user.


# change the value for a different result
# num = 7
# uncomment to take input from the user
# num = int(input("Enter a number: "))
def factorial_calc(num):
    factorial = 1

    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print('')
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f"The factorial of {num} is {factorial}")
