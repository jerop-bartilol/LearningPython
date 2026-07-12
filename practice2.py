registrationNumber=input("Enter Registration Number\n")
studentName=input("Enter student Name\n")
studentGender=input("Enter the student's gender\n")
unitName=input("Enter the Unit Name\n")
unitCode=input("Enter the Unit Code\n")
marks=float(input("Enter the marks\n"))

if marks>=70 and marks<=100:
    grade="A"
    comment="Excellent"
elif marks>=60 and marks <=69:
    grade="B"
    comment="Good"
elif marks>=50 and marks<=59:
    grade="C"
    comment="Fair"
elif marks>=40 and marks<= 49:
    grade="D"
    comment="Pass"
elif marks>=0 and marks<=39:
    grade="F"
    comment="Fail"
else:
    comment="Invalid marks"
    marks = float(input("Please enter the marks again (0-100): "))
    
#Printing Transcript
print(f"Registration Number\t{registrationNumber}\n")
print(f"Student Name\t{studentName}\n")
print(f"Student Gender\t{studentGender}\n")
print(f"Unit Name\t{unitName}\n")
print(f"Unit Code\t{unitCode}\n")
print(f"Marks\t{marks}\n")
print(f"Grade\t{grade}\n")
print(f"Comment\t{comment}\n")
