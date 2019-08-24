#Count variable , to track the no of triangles that contains origin
Count = 0


# reading the triangles.txt file line by line
for line in open('triangles.txt'):

    # split one line by coordinates
    ax, ay, bx, by, cx, cy = map(int, line.split(','))

    # check if the project euler formula satisfied
    a = ax*by - ay*bx > 0
    b = bx*cy - by*cx > 0
    c = cx*ay - cy*ax > 0

    Count += a==b==c


print("Number of triangles that contain the origin:", Count)