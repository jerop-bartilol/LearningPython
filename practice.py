basicSalary=float(input("Enter the basic salary\n"))
overTime=float(input("Enter Over time\n"))
if overTime >0 or overTime<50:
    overTime=overTime*300
else:
    overTime=overTime*350
grossPay= basicSalary+overTime
#Calculalting PAYE
if grossPay>=1 and grossPay<=30000:
    pass
elif grossPay>=30001 and grossPay<=50000:
    paye=0.15*grossPay
elif grossPay>=50001 and grossPay<=99999:
    paye=0.20*grossPay
elif grossPay>=100000 and grossPay<=150000:
    paye=0.25*grossPay
else:
    paye=0.30*grossPay
#Calculating deductions
nssf=0.06*grossPay
sha=0.027*grossPay
housingLevy=0.015*grossPay

#Calculating Net Pay
netPay=grossPay-(paye+nssf+sha+housingLevy)
#Output
print(f"Gross Pay\t{grossPay}\n")
print(f"P.A.Y.E is\t{paye}\n")
print(f"Net Pay is\t{netPay}")