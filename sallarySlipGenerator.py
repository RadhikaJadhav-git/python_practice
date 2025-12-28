basic = int(input("Enter basic salary: "))

hra = basic * 0.2
da = basic * 0.1
pf = basic * 0.12

net_salary = basic + hra + da - pf

print("Basic:", basic)
print("HRA:", hra)
print("DA:", da)
print("PF:", pf)
print("Net Salary:", net_salary)
