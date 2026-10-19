# #ask for name of students
student = ["James", "Kichwa", "Dennis", "Ronnex", "Vincent", "Rodgers"]
print(student)

for i in range(6):
    name= input(f"Enter the name of students {i+1}: ")
    student.append(name)

marks = [90, 76, 87, 88, 66, 79]
print(marks)

for i in range(6):
    mark= input(f"Enter mark for {student[i]}: ")
    marks.append(mark)

#displays all the students and their marks
print("/n--- Student marks ---")
for i in range(6):
    print(f"{student[i]}: {marks[i]}")

#calculate highest, lowest and average marks
highest_mark = max(marks)
lowest_mark = min(marks)
average_mark = sum(marks) / len(marks)

#Find students with highest and lowest marks
highest_mark = []
lowest_mark = []

for i in range(6):
    if marks[i] == highest_mark:
        highest_students.append(student[i])

    if marks[i] == lowest_mark:
        lowest_student.append(student[i])

#Displays results
print("\n--- Results ---")
print(f"Highest mark: {highest_mark} ")
print(f"Lowest mark: {lowest_mark} ")
print(f"Average mark: {average_mark:.2f} ")

