def positions(A):
    n = []
    # Add in a list (n) the position that the rectangle (A) pass by
    for i in range(A[0][0], A[1][0]+1):
        for j in range (A[0][1], A[1][1]+1):
            pos = (i,j)
            n.append(pos)
    return n

def Area(A, B):
    points = []
    n = positions(A)
    m = positions(B)

    #Count the number of equal positions = Area
    for i in range (len(n)):
        for j in range(len(m)):
            if n[i][0] == m[j][0] and n[i][1] == m[j][1]:
                points.append(n[i])
    return len(points)
  
A = "(3,5 ; 11,11)"
B = "(7,2 ; 13,7)"
C = "(11,11 ; 15,13)"

A = format(A)
B = format(B)
C = format(C)
print(Area(A, B))
print(Area(A, C))
