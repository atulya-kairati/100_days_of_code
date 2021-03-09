from random import randint

students = "Ramu shamu madarchod bhosdiwala bhadwa betichod".split(' ')

marks = {student: randint(10, 100) for student in students}
print(marks)
passed = {student: score for student, score in marks.items() if score >= 40}
print(f'Passed Students: {passed}')

######################################

print({name: len(name) for name in students})
######################################