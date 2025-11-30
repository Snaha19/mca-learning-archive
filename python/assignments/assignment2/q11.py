def CalculateSITcourseFees():
    print("SIT COURSE LIST")
    print("1. Btech \n2. BCA \n3. BBA \n4. BHHA \n5. BSc \n6. MBA \n7. MCA")

    course_code = int(input("Enter what course are you getting admission in (1 to 7): "))
    TIGans = int(input("Studied from TIG? 0 = No, 1 = Yes: "))
    entrance_test = int(input("Taken admission through valid rank? 0 = No, 1 = Yes: "))
    sex = int(input("Gender? 0 = Male, 1 = Female: "))

    # Course details
    if course_code == 1:
        course = "Btech"
        sem = 8
        adm = 100000
        rem = 75000

    elif course_code == 2:
        course = "BCA"
        sem = 8
        adm = 70000
        rem = 50000

    elif course_code == 3:
        course = "BBA"
        sem = 8
        adm = 70000
        rem = 50000

    elif course_code == 4:
        course = "BHHA"
        sem = 6
        adm = 60000
        rem = 45000

    elif course_code == 5:
        course = "BSc"
        sem = 6
        adm = 50000
        rem = 30000

    elif course_code == 6:
        course = "MBA"
        sem = 4
        adm = 140000
        rem = 100000

    elif course_code == 7:
        course = "MCA"
        sem = 4
        adm = 120000
        rem = 80000

    else:
        print("Invalid course id! Enter valid one.")
        return

    # Scholarship calculations
    if course_code <= 5:
        if TIGans == 1:
            sch1 = 10000
        else:
            sch1 = 0
    else:
        if TIGans == 1:
            sch1 = 15000
        else:
            sch1 = 0

    if entrance_test == 1:
        sch2 = 15000
    else:
        sch2 = 0

    if sex == 0:
        sch3 = 0
    else:
        sch3 = 10000

    # Apply scholarship
    adm = adm - (sch1 + sch2 + sch3)
    if adm < 0:
        adm = 0

    if TIGans == 1:
        rem = rem - sch1

    total = adm + rem * (sem - 1)

    print("Course selected:", course)
    print("Total course fee:", total)


# Function call
CalculateSITcourseFees()
