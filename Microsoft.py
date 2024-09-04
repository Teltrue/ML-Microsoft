def creditval(num):
    # Convert the number to a list of integers
    list_num = [int(digit) for digit in num]
    new_list = []

    # Start from the second to last digit and move backwards
    for index, digit in enumerate(reversed(list_num)):
        if index % 2 == 1:  # Double every second digit
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            new_list.append(doubled)
        else:
            new_list.append(digit)

    # Calculate the sum of the processed numbers
    lisum = sum(new_list)

    # Check if the total modulo 10 is 0
    if lisum % 10 == 0:
        print("Credit card is valid")
    else:
        print("Error, credit card invalid")


credit = input('Enter Credit card number: ')  # Keep as a string to maintain leading zeros
creditval(credit)



