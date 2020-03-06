# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.

name = input("Please enter your name: ")
print(f"Hello, {name}.")
number = int(input("Please enter a number: "))
print(f"You've entered {number}.")


# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.

is_fizz = number%3 == 0
is_buzz = number%5 == 0

# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************

if is_fizz and is_buzz:
    print(f"{number} is a FizzBuzz number.")
elif is_fizz: 
    print(f"{number} is a Fizz number.")
elif is_buzz:
    print(f"{number} is a Buzz number.")
else:
    print(f"{number} is neither a fizzy or a buzzy number.")























