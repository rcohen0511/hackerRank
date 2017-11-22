def findCircleNum(students):
    total_circles = 0
    len_students = len(students)
    visited_set = set()

    def dfs(n):
        for x in range(len_students):
            if students[n][x] == 'Y' and x not in visited_set:
                visited_set.add(x)
                dfs(x)

    for x in range(len_students):
        if x not in visited_set:
            total_circles += 1
            dfs(x)
    return total_circles


# On hackerRank site need to use sys.stdin to build array:
# import sys
# students = []
# for line in sys.stdin:
#     students.append(line)
# M = students[1:]

# uncomment differnt M's for different test cases
# M = ['YYNNN', 'YYYNN', 'NYYNN', 'NNNYY', 'NNNYY']
M = ['YYNNNN', 'YYYNNN', 'NYYNNN', 'NNNYYN', 'NNNYYN', 'NNNNNY']
print(findCircleNum(M))