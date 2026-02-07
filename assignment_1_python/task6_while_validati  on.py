## TASK 6: While Loop and Input Validation

marks = []

while True:
    score = float(input("Enter marks between 0 and 100: "))

    if 0 <= score <= 100:
        marks.append(score)

        break
    else:
        print("Invalid input. Please enter a valid score.")

print("Valid Marks Entered:", marks)

