

def findCircleNum(M):
    cnt = 0
    N = len(M)
    vset = set()

    def dfs(n):
        for x in range(N):
            print(M[n][x])
            if M[n][x] == 'Y' and x not in vset:
                print('if true')
                vset.add(x)
                dfs(x)

    for x in range(N):
        if x not in vset:
            cnt += 1
            dfs(x)
    return cnt

M = ['YYNNN', 'YYYNN', 'NYYNN', 'NNNYY', 'NNNYY']
M = ['YYNNNN', 'YYYNNN', 'NYYNNN', 'NNNYYN', 'NNNYYN', 'NNNNNY']
# M = [[1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]

print(findCircleNum(M))

# students = ['4', 'YYNNN', 'YYYNN', 'NYYNN', 'NNNYY','NNNYY']
# # students = ['5','YNNNN','NYNNN', 'NNYNN', 'NNNYN', 'NNNNY']
# print(analyseStudents(students))