def analyseStudents(students):
    students = students[1:]
    numStudents = len(students)
    numCircles = 0

    circles = []


    for student in range(numStudents):
        print('checking student i: '+str(student))
        for friend in range(len(student)):
            print(friend)





students = ['4', 'YYNNN', 'YYYNN', 'NYYNN', 'NNNYY','NNNYY']
# students = ['5','YNNNN','NYNNN', 'NNYNN', 'NNNYN', 'NNNNY']
print(analyseStudents(students))