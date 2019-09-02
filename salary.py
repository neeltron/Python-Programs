name = input("Enter your name: ")
bas_sal = int(input("Enter the basic salary: "))
hra = bas_sal * 20 / 100
da = bas_sal * 12 / 100
nps = bas_sal * 5 / 100
cpf = bas_sal * 12 / 100
ac_al = 1000
ta = bas_sal * 5 / 100
inc_tax = bas_sal * 20 / 100
net_sal = bas_sal + hra + da + nps + cpf + ac_al + ta - inc_tax
print("Hey", name+",\nYour net salary is",net_sal)
