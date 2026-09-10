m = [[1,4,7],[0,3,6]]

def maior(m):
    max = m[0][0]
    imax = 0
    jmax = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > max:
                max = m[i][j]
                jmax = j
                imax = i
    return max,imax,jmax

print(maior(m))
