import math
# Create loop for calculator
loop = True
# value is current value stored ,
value = [0]
# cycle is the amount of calculations done so far
cycle = 0
# sum is all values added together
sum = float()

while loop:
    # provide list and visual format
    # RESULT is the previous value
    RESULT = value[cycle]
    print(f"Current Result: {float(value[cycle])}\n")
    print("Calculator Menu")
    print('-' * 15)
    print("0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation")
    print("6. Logarithm\n7. Display Average\n")
    small_loop = True
    while small_loop:
        select = int(input("Enter Menu Selection: \n"))
        if select == 0:
            print("Thanks for using this calculator. Goodbye!")
            small_loop = False
            loop = False
        # Get inputs
        elif 1 <= select <= 6:
            cycle += 1
            one = (input("Enter first operand: \n"))
            two = (input("Enter second operand: \n"))
            # If "RESULT", Give RESULT
            if one == "RESULT":
                one = RESULT
            if two == "RESULT":
                two = RESULT
            one = float(one)
            two = float(two)
            # Calculate accordingly
            if select == 1:
                value.append(one + two)
            elif select == 2:
                value.append(one - two)
            elif select == 3:
                value.append(one * two)
            elif select == 4:
                value.append(one / two)
            elif select == 5:
                value.append(math.pow(one, two))
            elif select == 6:
                value.append(math.log(two, one))
            small_loop = False

        # Provide Statistics including Sum of calculations, counter, and average of calculations
        elif select == 7:
            if cycle > 0:
                for i in value:
                    sum += i
                count = float(cycle)
                print(f"Sum of calculations: {sum}")
                print(f"Number of calculations: {cycle}")
                print(f"Average of calculations: {(round(sum / count, 2)) }")
            # Print error message if no calculations done
            elif cycle == 0:
                print("Error: No calculations yet to average!")

        # Provide Error if invalid
        else:
            print("Error: Invalid selection!\n")
