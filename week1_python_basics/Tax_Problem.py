#Tax Calculator Problem

# Level 1: Input & Gross Salary Calculation
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic monthly salary (₹): "))
special_allowance = float(input("Enter special monthly allowance (₹): "))
bonus_percent = float(input("Enter annual bonus % of gross salary: "))

gross_monthly_salary = basic_salary + special_allowance
annual_gross_salary = (gross_monthly_salary * 12) + ((bonus_percent / 100) * (gross_monthly_salary * 12))

# Level 2: Taxable Income
standard_deduction = 50000
taxable_income = annual_gross_salary - standard_deduction

# Level 3: Tax Calculation (Using Provided Block)
tax = 0
rebate = 0

if taxable_income <= 300000:
    tax = 0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = 15000 + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = 45000 + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = 90000 + (taxable_income - 1200000) * 0.20
else:
    tax = 150000 + (taxable_income - 1500000) * 0.30

# Rebate under 87A
if taxable_income <= 700000:
    rebate = tax
    tax = 0

# Cess and Final Tax
cess = tax * 0.04
total_tax = tax + cess

# Level 4: Net Salary
net_salary = annual_gross_salary - total_tax

# Level 5: Final Report (Your Exact Format)
print("\n==================== EMPLOYEE TAX REPORT ====================")
print(f"Employee Name      : {name}")
print(f"Employee ID        : {emp_id}")
print(f"Gross Monthly Salary: ₹{gross_monthly_salary:,.2f}")
print(f"Annual Gross Salary : ₹{annual_gross_salary:,.2f}")
print(f"Standard Deduction  : ₹{standard_deduction:,.2f}")
print(f"Taxable Income      : ₹{taxable_income:,.2f}")
print(f"Base Tax            : ₹{tax:,.2f}")
print(f"Cess (4%)           : ₹{cess:,.2f}")
print(f"Total Tax Payable   : ₹{total_tax:,.2f}")
print(f"Annual Net Salary   : ₹{net_salary:,.2f}")
