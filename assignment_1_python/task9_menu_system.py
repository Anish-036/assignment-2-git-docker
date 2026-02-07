# TASK 9 : Menu System

student = {}

marks = []

def enter_details():
    student['name'] = input("Enter student name: ")
    student["semester"] = input("Enter semester: ")

def enter_marks():
    marks.clear()
    
    for i in range(3):
        marks.append(float(input(f"Marks {i+1}: ")))

def view_summary():
    average = sum(marks)/len(marks) 
    print("Name:", student.get('name'))
    print("Average Marks:", average)


while True:
    print("\n1. Enter Details \n2. Enter Marks \n3. View Summary \n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        enter_details()
    elif choice == '2':
        enter_marks()
    elif choice == '3':
        view_summary()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
    