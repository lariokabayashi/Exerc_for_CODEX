def transform_int(l):
    # Transform string in int
    num,  incr = 0, 1
    for n in range(len(l)-1, -1, -1):
        if l[n].isnumeric():
            num += int(l[n])*incr
            incr = incr*10
    return num

def sep(x):
    li, lj = [], []
    formatted_A = []
    #Setting variables
    k = 0
    # Separating i from (i,j)
    while x[k] != ",":
        li.append (x[k])
        k += 1
    # Separating j from (i,j)
    while k+1 < len(x):
        lj.append (x[k+1])
        k += 1

    formatted_A.append(transform_int(li))
    formatted_A.append(transform_int(lj))
    return formatted_A

def format(A):
    # Format the rectangle in a tuple ()
    formatted_A = []
    b = A.split(";")
    for x in range(len(b)):
        formatted_A.append(sep(str(b[x])))
    return formatted_A

def positions(A):
    n = []
    # Add in a list (n) the position that the rectangle (A) pass by
    for i in range(A[0][0], A[1][0]+1):
        for j in range (A[0][1], A[1][1]+1):
            pos = (i,j)
            n.append(pos)
    return n

def intersects(A, B):
    
    n = positions(A)
    m = positions(B) 

    # See if there is any equal position between rectangle A and B
    for i in range (len(n)):
        for j in range(len(m)):
            if n[i][0] == m[j][0] and n[i][1] == m[j][1]:
                return True
    return False

A = "(3,5 ; 11,11)"
B = "(7,2 ; 13,7)"
C = "(11,11 ; 15,13)"

A = format(A)
B = format(B)
C = format(C)
print(intersects(A, B))
print(intersects(A, C))
print(intersects(B, C))
    
