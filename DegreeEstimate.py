name = input("Enter Your name : ")

student_number = input("Enter your Student Number : ")

degreeDuration = int(input("Enter the Duration of your Degree : "))

if not student_number.isdigit() and len(student_number):
    print("The Student Number must be a Digit")

else:

 year_of_reg = int(student_number[0:2])

 yearStart = year_of_reg + 1

 GraduationYear = 2000 + (degreeDuration + yearStart)

 print("Hello "+ name +" You are going to graduate in "+str(GraduationYear))





