import os
import sys

def gradingStudents(grades):
    final = []
    for grade in grades:
        if grade<38 or grade%5 < 3:
            final.append(grade)
        else:
            #if grade%5 > 0:
            final.append(5*(grade//5)+ 5 if grade%5 > 0 else 0)
    return(final)


grades = [73,67,38,33]
print(gradingStudents(grades))
