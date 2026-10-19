students=[]
marks=[]
number_of_entries=0

while number_of_entries < 5:
    student_name=input("Enter name of student: ")
    student_marks=float(input("Enter student marks: "))

    marks.append(student_marks)
    students.append(student_name)
    number_of_entries +=1
    continue

for i in range(len(students)):
    print(students[i], "-", marks[i])
    

highest_marks=max(marks)
lowest_mark=min(marks)
average_marks=sum(marks)/len(marks)

print("Highest marks: ",highest_marks)
print("Lowest marks: ", lowest_mark)
print("Average marks: ", average_marks)

#block executing highest student
index_of_highest_mark=marks.index(highest_marks)

student_with_highest_marks=students[index_of_highest_mark]

print("Student with highest marks: ", student_with_highest_marks)

#block executing lowest student
index_of_lowest_marks=marks.index(lowest_mark)

student_with_lowest_marks=students[index_of_lowest_marks]
print("Student with lowest marks: ", student_with_lowest_marks)


#grading scores 
distintion= 0
pass_= 0
fail= 0

for mark in marks:
    if mark>=70:
        distintion+=1

    elif mark>= 55:
        pass_+=1

    else:
        fail= fail+1

print("Distinction: ", distintion)
print("Pass: ", pass_)
print("fail: ", fail)