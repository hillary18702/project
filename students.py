
students=[
    {
        "name": "Hillay",
        "grade": "Grade 9",
        "scores": {
            "math": 70,
            "eng": 90,
            "kis": 55
        }
    },
    {
        "name": "Ouma",
        "grade": "Grade 2",
        "scores": {
            "math": 76,
            "eng": 47,
            "kis": 55
        }
    }
]
# print(students[1]["scores"]["math"])
# print("Before: ", students)

# students[0]["name"]="Hillary Oswago"

# print("After: ", students)

# students["date_of_birth"]="1999-10-09"
# students["height"] =2.4

# average=sum(students["scores"])/len(students["scores"])
# print(students)
# print("Average score: ", average)
# students.pop("grade")
# print(students)


name=input("Enter full name: ")
sex = input("Enter sex(male or female): ")
grade=input("Enter grade as a number: ")
county=input("Enter the student's county: ")
sub_county=input("Enter the student's sub-county: ")
math=float(input("Enter the student's Math score: "))
eng=float(input("Enter the student's English score: "))
kis=float(input("Enter the student's Kiswahili score: "))
science=float(input("Enter the student's Science score: "))
sss_cre=float(input("Enter the student's Social Studies & CRE score: "))

students_list=[
    {
        "name": "Ouma Arera",
        "sex": "male",
        "grade": 7,
        "county": "omabei",
        "sub-county": "Karachuonyo",
        "subjects": {
            "math": 70,
            "eng": 66,
            "kis": 57,
            "science": 34,
            "ss_cre": 47
        }
    },
    {      "name": "Faith Atieno",
            "sex": "female",
            "grade": 7,
            "county": "omabei",
            "sub-county": "Karachuonyo",
            "subjects": {
                "math": 75,
                "eng": 56,
                "kis": 47,
                "science": 54,
                "ss_cre": 50
        }
    },
    {

    }
]

subject= {
        "math": math,
        "eng": eng,
        "kis": kis,
        "science": science,
        "ss_cre": sss_cre
    }

students_list[2]["name"]=name
students_list[2]["sex"]=sex
students_list[2]["grade"] = grade
students_list[2]["county"] = county
students_list[2]["sub-county"]=sub_county
students_list[2]["subjects"]=subject

print(students_list)

for stud in students_list:
    print("Student: ", stud)
    total_score = stud["subjects"]['math'] + stud['subjects']['eng'] + stud['subjects']['kis'] + stud['subjects']['science'] + stud['subjects']['ss_cre']
    students_list[students_list.index(stud)]["total"]=total_score

print(students_list)

#ranking students from highest to lowest

# Highest scoring student
highest_student = max(students_list, key=lambda stud: stud["total"])

# Lowest scoring student
lowest_student = min(students_list, key=lambda stud: stud["total"])

print("HIGHEST SCORING STUDENT ")
print("Name:", highest_student["name"])
print("Total score:", highest_student["total"])

print("LOWEST SCORING STUDENT ")
print("Name:", lowest_student["name"])
print("Total score:", lowest_student["total"])

#Best student per subject

# Best student in each subject
subjects = ["math", "eng", "kis", "science", "ss_cre"]

print("BEST STUDENT PER SUBJECT")

for sub in subjects:
    best_student = max(
        students_list,
        key=lambda stud: stud["subjects"][sub]
    )

    print(
        f"Subject: {sub.upper()} | "
        f"Student: {best_student['name']} | "
        f"Score: {best_student['subjects'][sub]}"
    )

