import time
numbers = []
greater_than_average = [] 
print("Welcome to my average calculator! Insert numbers or say 'done'! :)")
while len(numbers) < 5:
    raw = input("Please enter a number: ")
    if not raw:
        print("Input cannot be empty.")
        time.sleep(1)
        continue
    if raw.lower().strip() == "done":
        if not numbers:
                print("Insert atleast 1 number!")
                time.sleep(1)
                continue
        break

    try:
        user = float(raw)
    except ValueError:
        print("Input only numbers or 'done'!")
        time.sleep(1)
        continue
    if user in numbers:
        print("Select a different number please!")
        time.sleep(1)
        continue
    numbers.append(user)
if not numbers:
    print("Insert atleast 1 number!")
else: 
    average = sum(numbers)/len(numbers)
    for number in numbers:
        if number > average:
            greater_than_average.append(number)
    print(f"Here is your average: {average}")
    time.sleep(0.5)
    print(f"Greater than average numbers: {greater_than_average}")
