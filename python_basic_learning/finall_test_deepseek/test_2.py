# There is a dictionary containing students' grades.
# grades = {'Kim': 85, 'Lee': 72, 'Park': 90, 'Choi': 68, 'Jung': 95}
# Print the grade (A, B, C, D, F) based on each student's score.
grades = {'Kim': 85, 'Lee': 72, 'Park': 90, 'Choi': 68, 'Jung': 95}
for name, grade in grades.items():
    if grade >= 90:
        print(f"{name}: {grade} -> A")
    elif grade >= 80:
        print(f"{name}: {grade} -> B")
    elif grade >= 70:
        print(f"{name}: {grade} -> C")
    elif grade >= 60:
        print(f"{name}: {grade} -> D")
    else:
        print(f"{name}: {grade} -> F")