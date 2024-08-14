def edit_distance(s1, s2):
# add a blank character for both strings
    m=len(s1)+1
    n=len(s2)+1
# launch a matrix
    tbl = [[0] * n for i in range(m)] 
    for i in range(m): tbl[i][0]=i
    for j in range(n): tbl[0][j]=j

    for i in range(1, m):
        for j in range(1, n):
#if strings have same letters, set operation cost as 0 otherwise 1
            cost = 0 if s1[i-1] == s2[j-1] else 1
#find min practice
            tbl[i][j] = min(tbl[i][j-1]+1, tbl[i-1][j]+1, tbl[i-1][j-1]+cost)
    print(i,j)
    return tbl

edit_distance("birthday", "Birthdayyy")