## TASK 5: Loops and Iteration


n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    score = float(input(f"Enter marks for subject {i+1}: "))

    marks.append(score)

print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks)/n)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
