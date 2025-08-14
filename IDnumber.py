Id_no = input("Enter your ID Number : ")

if (len(Id_no) == 13) and (Id_no.isdigit() == True):
    year = Id_no[0:2]
    year = int(year)


    if year > 25:
        year_prefix = "19"
    else:
        year_prefix = "200"

    year =  year_prefix + str(year)
    
    month = Id_no[2:4]

    month = int(month)

    if month > 0 and month < 13:
        match month :
            case 1 :
                month = "January"
            case 2 :
                month = "February"
            case 3 :
                month = "March"
            case 4 :
                month = "April"
            case 5 :
                month = "May"
            case 6 :
                month = "June"
            case 7 :
                month = "July"
            case 8 :
                month = "August"
            case 9 :
                month = "September"
            case 10 :
                month = "October"
            case 11 :
                month = "November"
            case 12 :
                month = "December"
            case _:
                print("Invalid Birth Month")
        
        day = Id_no[4:6]

        gender = Id_no[6:10]
        gender = int(gender)

        if gender > 0 and gender <5000 :
            gender = "Female"
        else:
            gender = "Male"
        
        citizen = Id_no[10:11]
        citizen = int(citizen)

        if citizen == 0 :
            citizen = "SA Citizen"
        else:
            citizen = "Permanet Citizen"
else:
    print("Invalid ID Number")

print("Birth Year : " + year)
print("Birth Month : " + month)
print("Birth Day : " + day)
print("Gender : " + gender)
print("Citizen : " + citizen)
