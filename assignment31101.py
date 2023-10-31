numbers = []
while True:
    user_input = input("Enter an integer (or 'done' to finish): ")
    
    if user_input == 'done':
        break

    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if numbers:
    average = sum(numbers) / len(numbers)
    print("Average value:", average)
else:
    print("Bye")