s=int(input("Enter the student's marks : "))
if s>=90 and s<=100:
    print("Grade: A+")  

elif s>=80 and s<=89:
    print("Grade: A")

elif s>=70 and s<=79:
    print("grade: B")

elif s>=60 and s<=69:
    print("grade : C")

elif s>=50 and s<=59:
    print("grade :D")

elif s<50:
    print("grade :Fail")

else:
    print("Invalid marks entered. Please enter a value between 0 and 100.")

