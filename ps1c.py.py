# ps1c.py
# Assignment 1 - Part C
# Name: Your Name
# Collaborators: None

# Input
starting_salary = float(input("Enter the starting salary: "))

# Constants
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
annual_return = 0.04
semi_annual_raise = 0.07
months = 36

# Bisection search setup
low = 0
high = 10000  # represent 0.0000 to 1.0000
steps = 0
epsilon = 100  # within $100 accuracy
best_rate = None

# Check if impossible
current_savings = 0
annual_salary = starting_salary

for m in range(1, months + 1):
    monthly_salary = annual_salary / 12
    current_savings += current_savings * (annual_return / 12)
    current_savings += monthly_salary  # saving 100%
    
    if m % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

if current_savings < down_payment - epsilon:
    print("It is not possible to pay the down payment in three years.")
else:
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        portion_saved = mid / 10000
        
        # simulate savings
        current_savings = 0
        annual_salary = starting_salary
        
        for m in range(1, months + 1):
            monthly_salary = annual_salary / 12
            current_savings += current_savings * (annual_return / 12)
            current_savings += monthly_salary * portion_saved
            
            if m % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise
        
        if abs(current_savings - down_payment) <= epsilon:
            best_rate = portion_saved
            break
        elif current_savings < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)
