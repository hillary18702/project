#ask the user to enter rheir gross salary
gross_pay=float(input("Enter the gross salary: "))

#calculate the deductions 
housing_levy=gross_pay * 0.015
nssf = gross_pay * 0.03
sha = gross_pay * 0.02
net_pay =0
paye=0

# taxable_income= gross_pay- housing_levy-nssf-sha

#calculating taxable pay 
taxable_pay = gross_pay - housing_levy - nssf - sha

if taxable_pay <= 20000:
    paye = taxable_pay * 0.10
    print("paye: ", paye)

elif taxable_pay <= 40000:
    paye = (20000*0.10) + ((taxable_pay -20000)* 0.15)
    print("paye: ", paye)

elif taxable_pay <= 100000:
    paye = (200000*0.10) + (19999*0.15) + ((taxable_pay-40000)* 0.2)
    print("paye: ", paye)

elif taxable_pay <= 300000:
    paye = (200000*0.10)+ (19999*0.15)+ (59999*0.2)+ ((taxable_pay-100000)*0.25)
    print("paye: ", paye)

elif taxable_pay <= 500000:
    paye = (200000*0.10)+ (19999*0.15)+ (59999*0.2)+ (199999*0.25) + ((taxable_pay-300000)*0.3)
    print("paye: ",paye)

else:
    paye=(200000*0.10)+ (19999*0.15)+ (59999*0.2)+ (199999*0.25) + (199999*0.3) + ((taxable_pay-500000)*0.35)
    print("paye: ", paye)

print("SHA: ", sha)
print("NSSF: ", nssf)
print("Housing Levy: ", housing_levy)
print("Net Pay: ", taxable_pay-paye )
