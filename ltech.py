# We want to create a list of students
student_sought=input("Enter the student you're looking for: ")

list_of_students=["Kamau", "Morgan", "Ochieng'", "Wanjala", "Mogaka"]
print(list_of_students)
print(list_of_students[-1])


list_of_students.append("Mary")
print(list_of_students)
list_of_students[1]="Ojwang'"
print(list_of_students)

# Remove elements from a list
list_of_students.pop(0)
print(list_of_students)

list_of_students.remove("Mary")
print(list_of_students)



for student in list_of_students:
    if student == student_sought:
        print("I found ", student_sought)

    else:
        print(f"{student_sought} not found!")