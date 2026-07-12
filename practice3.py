registrationNumber=input("Enter the registartion number\n")
depatureTime=input("Enter the depature Time")

if registrationNumber=="KBZ 009z" and depatureTime=="11:00":
    destination="Voi"
    arrivalTime="12:00"
    available=False
elif registrationNumber=="KBX 100x" and depatureTime=="9:00":
    destination="Kisumu"
    arrivalTime="12:00"
    available=False
elif registrationNumber=="KAQ 998y" and depatureTime=="8:00":
    destination="Mombasa"
    arrivalTime="2:00"
    available=False
else:
    available=True
if available==False:
    print(f"{destination} not available")
    


