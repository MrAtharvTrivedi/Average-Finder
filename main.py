# Author ---> Atharv Trivedi
# This is a average calculator program built using Python.


# Defining a function to calculate the average of the two numbers entered by the user
def avgnum(num1, num2):
    average = ((num1+num2)/2)
    return average 

while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Checking if the inputs provided by user are numbers or not
    if num1.isdigit() and num2.isdigit():
        num1 = float(num1)  # Typecasting num1 to a floating point number.  
        num2 = float(num2)  # Typecasting num2 to a floating point number.
        avg = avgnum(num1, num2)    # Calling a avgnum function
        print(avg)  # Printing the average of the two numbers
        quit()  # Quitting the program after the average is printed
    else:
        print("Kindly enter a number only")

