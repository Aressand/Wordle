name_s = ""
grade_s = 0 # AL posto di 0, potrei mettere un valore più piccolo come ad esempio un -10.


for i in range(10):
    name = input("Name: ")
    grade = int(input("Grade:"))
    if grade > grade_s:  # Per esempio se uno studente avesse preso 0, non sarebbe maggiore del grade_s e quindi sarebbe scartato
        grade_s = grade
        name_s = name

print(f"The higher grade was {name_s} with {grade_s}")
