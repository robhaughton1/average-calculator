import time
numbers = []
greater_than_average = []
try:
    while len(numbers) < 5:
        raw = input("Enter a number: ")

        if not raw:
            print("Message cannot be empty.")
            time.sleep(1)
            continue

        try:
            user = float(raw)
        except ValueError:
            print("Input only numbers.")
            time.sleep(1)
            continue

        numbers.append(user)

    average = sum(numbers)/len(numbers)
    for number in numbers:
        if number > average:
            greater_than_average.append(number)

except Exception as e:
    print(f"Error: {e}")
    
print(f"Here is your average: {average}")
time.sleep(0.5)
print(f"And here are the numbers greater than the average: {greater_than_average}")
