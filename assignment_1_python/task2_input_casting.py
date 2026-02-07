## TASK 2: User, Input Casting

income = float(input("Enter your monthly income: "))

expenses = float(input("Enter your monthly expenses: "))

savings = income - expenses

if savings > 0:

    print("Savings:", savings)
else:
    print("Deficit",savings)


### REASONING QUESTION ANSWER:

#1 >> Python checks types at runtime to allow flexibility and faster process.
#2 >> Unvalidated input can cause incorrect billing, fraud and system crashes.