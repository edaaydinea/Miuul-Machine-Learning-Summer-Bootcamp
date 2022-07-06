"""
Write divide_students function.
Save the students to the list if the student's index is even.
Save the students to the another list if the student's index is odd.
Return the these two list as one list.
"""

students = ["John", "Mark", "Vanessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    return groups


if __name__ == '__main__':
    print(divide_students(students))
