# TASK 4: Branching and Conditional Statements

attendance = float(input("Attendance percentage: "))
marks = float(input("Total Marks obtained: "))

if attendance >= 75 and marks >= 50:
    print("Passed")
else:
    print("Failed ")


cgpa = float(input("Enter your CGPA: "))
income = float(input("Family monthly income: "))

if cgpa >= 3.2 and income < 50000 and attendance >= 80:
    print("Eligible for scholarship")
elif cgpa >= 3.2 and income < 50000 and attendance < 50:
    print("50% Scholarship")
else:
    print("Not eligible for scholarship")







