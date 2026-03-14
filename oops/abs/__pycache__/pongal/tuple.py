students = (
    (101, "Ravi", 20),
    (102, "Sita", 21),
    (103, "sai", 22),
    (104, "Kiran", 20),
    (105, "Neha", 23)
)
new_student = (103, "sai", 22)
found = False
for student in students:
    if student == new_student:
        found = True
        break
if found:
    print("Record already exists")
else:
    print("New record, can be added")