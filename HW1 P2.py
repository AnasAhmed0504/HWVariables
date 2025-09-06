name1 = input("Enter the first student's name: ")
id1 = input("Enter the first student's id: ")
grade1 = float(input("Enter the first student's grade: "))

name2 = input("Enter the second student's name: ")
id2 = input("Enter the second student's id: ")
grade2 = float(input("Enter the second student's grade: "))

print('Informat for students and their "MATH" grades')

print(name1, "(id" + id1,") got grade", grade1)
print(name2, "(id" + id2,") got grade", grade2)

print("Average math's grades is", (grade1 + grade2) / 2)
