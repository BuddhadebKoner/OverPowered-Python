'''
2. Write a Python program to find the gross salary of an employee.
If basic salary is less than Rs. 15000/- then DA= Rs. 1200/-
and HRA = 12% of basic. Otherwise, DA=15% and HRA= 29% of basic salary.
Consider basic salary is user input.
Gross salary = Basic salary + DA + HRA

DA: Dearness Allowance
HRA: House Rent Allowance

'''
basicsalary = float(input("Enter the basic salary:"))

if basicsalary < 15000:
    da = 1200
    hra = 0.12 * basicsalary
else:
    da = 0.15 * basicsalary
    hra = 0.29 * basicsalary


print("The gross salary ",(basicsalary + da + hra))
