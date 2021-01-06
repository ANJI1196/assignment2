#Student Progress Report App:
rollno=int(input("Enter your Roll Number:"))
name=str(input("Enter student Name:"))
sub1=int(input("Enter Subject1 Marks:"))
sub2=int(input("Enter Subject2 Marks:"))
sub3=int(input("Enter Subject3 Marks:"))
sub4=int(input("Enter Subject4 Marks:"))
sub5=int(input("Enter Subject5 Marks:"))
sub6=int(input("Enter Subject6 Marks:"))
Total_marks=sub1+sub2+sub3+sub4+sub5+sub5
avg=Total_marks/6
print("Roll Number:",rollno)
print("Student Name:",name)
print("Total Marks:",Total_marks)
print("Average:",avg)
if avg>=80 and avg<=100:
    print("Your Grade is A")
elif avg>=79 and avg<60:
    print("Your Grade is B")
elif avg>=59 and avg<50:
    print("Your Grade is C")
elif avg>=49 and avg<40:
    print("Your Grade is D")
else:
    print("Promoted")
