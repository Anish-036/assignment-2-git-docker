# TASK 8 : Functions

def calculate_average(marks):

    return sum(marks)/len(marks)


def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return "NG"
    
def format_output(average, grade):
    return f"Average Marks: {average:.2f}, Grade: {grade}"

marks = [85, 92, 78, 88, 90]
avg = calculate_average(marks)
grade = determine_grade(avg)

print(format_output(avg, grade))

## REASONING QUESTION ANSWER:
# Returning values allows reuse and better program control than printing.