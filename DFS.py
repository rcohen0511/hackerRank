def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """

    # convert YYYNNN format to [[1,1,0],[1,0,1]]
    new_m = []
    temp_list = []
    M = M[1:]
    for i in range(len(M)):
        print(i, M[i])
        for x in range(len(M[i])):
            print(M[i][x])
            if M[i][x] == 'Y':
                temp_list.append(1)
            else:
                temp_list.append(0)
        new_m+=[temp_list]
        temp_list = []
        print(new_m)

    M = new_m
    cnt, N = 0, len(M)
    vset = set()
    def dfs(n):
        for x in range(N):
            if M[n][x] and x not in vset:
                vset.add(x)
                dfs(x)
    for x in range(N):
        if x not in vset:
            cnt += 1
            dfs(x)
    return cnt


students = ['4', 'YYNNN', 'YYYNN', 'NYYNN', 'NNNYY','NNNYY']
# students = ['5','YNNNN','NYNNN', 'NNYNN', 'NNNYN', 'NNNNY']
print(findCircleNum(students))