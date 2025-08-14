number = input("Enter the number to Calculate : ")

counter = 1

sum = 0


if not number.isdigit():
    print("The Number is not a digit")

else:
    number = int(number)
    while counter <= number :
        sum += counter
        counter += 1
        if counter > number :
            break

    print("Sum is : " + str(sum))

