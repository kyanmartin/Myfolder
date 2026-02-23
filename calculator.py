print("Calculator is running!")
thing_to_do = (input("Are you going to mutiply, divide, add or subtract? (*,/,+,-) "))
while thing_to_do not in ["*", "/", "+", "-"]:
    thing_to_do = input("Invalid operation. Please choose one of the following: (*, /, +, -):")
first_number = float(input("What is the first number? "))
second_number = float(input("What is the second number? "))
if thing_to_do == "/" and second_number == 0:
    print("Error: Division by zero is not allowed.")
else:
    answer = first_number * second_number if thing_to_do == "*" else \
        first_number / second_number if thing_to_do == "/" else \
        first_number + second_number if thing_to_do == "+" else \
        first_number - second_number if thing_to_do == "-" else "Invalid operation"

    print("The answer is: " + str(answer))
go_again = input("Do you want to go again? (y/n) ")
while go_again not in ["y", "n"]:
    go_again = input("Invalid input. Please enter 'y' for yes or 'n' for no: ")
if go_again == "y":
    print("Restarting the calculator...")
    exec(open("calculator.py").read())
else:
    print("Goodbye!")