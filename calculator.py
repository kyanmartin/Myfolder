print("Calculator is running!")
thing_to_do = (input("Are you going to mutiply, divide, add or subtract? (*,/,+,-) "))
while thing_to_do not in ["*", "/", "+", "-"]:
    thing_to_do = input("Invalid operation. Please choose one of the following: (*, /, +, -):")
first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))
answer = first_number * second_number if thing_to_do == "*" else \
        first_number / second_number if thing_to_do == "/" else \
        first_number + second_number if thing_to_do == "+" else \
        first_number - second_number if thing_to_do == "-" else "Invalid operation"
print("The answer is: " + str(answer))
