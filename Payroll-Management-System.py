def calculate_bonus(base_salary, Performace_rating): 
    if Performace_rating == 5: bonus_amount = base_salary * 0.20
    elif Performace_rating == 3 or 4: bonus_amount = base_salary * 0.10
    else : bonus_amount = 0 
    return bonus_amount

def calculate_tax(gross_salary):
    if gross_salary > 7000: tax_amount = gross_salary * 0.15
    elif gross_salary >= 3000 or gross_salary <= 7000: tax_amount = gross_salary * 0.10
    else: tax_amount = 0
    return tax_amount

def main_hr_app():
    Employee_name = input("Enter employee name: ")
    Employee_Debartment = input("Enter employee Debartment: ")
    Employee_BaseSalary = float(input("Enter employee Base Salary: "))
    if Employee_BaseSalary <=0 : print("Invalid Base Salary")
    Employee_Performace_rating = int(input("Enter employee Performace Rating: "))
    if Employee_Performace_rating >5 or Employee_Performace_rating <1 : print("Invalid Performace Rating")
    bonus = calculate_bonus(Employee_BaseSalary, Employee_Performace_rating)
    gross_salary = Employee_BaseSalary + bonus
    tax_amount = calculate_tax(gross_salary)
    net_salary = gross_salary - tax_amount

    print("-"*20)
    print(f"Payroll Statement for : {Employee_name}")
    print("-"*20)
    print(f"Employee Department : {Employee_Debartment}")
    print(f"Employee Base Salary: {float(Employee_BaseSalary)}EGP")
    print(f"Employee Performace Rating : {Employee_Performace_rating}")
    print(f"Employee Bonus : {float(bonus)}EGP")
    print(f"Employee Gross Salary : {float(gross_salary)}EGP")
    print(f"Employee Tax Amount : {float(tax_amount)}EGP")
    print(f"Employee Net Salary : {float(net_salary)}EGP")
    
main_hr_app()