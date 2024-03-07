result = None
operand = None
operator = None
wait_for_number = True

allow_operators = ["+", "-", "*", "/"]

while True:
    user_input = input(">>> ")

    if wait_for_number:
        try:
            user_input = float(user_input)
        except ValueError:
            print(f"'{user_input}' is not a number. Try again.")
            continue
        else:
            wait_for_number = False
            operand = user_input

            if result == None:
                result = operand

            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                result /= operand
            elif operator == None:
                continue
    else:
        if user_input == "=":
            print(f"Result: {result}")
            break
        elif user_input not in allow_operators:
            print(f"'{user_input}' is not '+' or '-' or '/' or '*'. Try again")
            continue
        else:
            wait_for_number = True
            operator = user_input
