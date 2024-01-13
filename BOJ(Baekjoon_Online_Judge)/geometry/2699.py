P = int(input())  # Read the number of test cases
test_cases = []

for _ in range(P):
    N = int(input())  # Number of grid points
    points = []
    while len(points) < N:
        line = input()
        line_points = line.split()
        for i in range(0, len(line_points), 2):
            x, y = int(line_points[i]), int(line_points[i + 1])
            points.append((x, y))
    test_cases.append(points)

def ccw(x1,y1,x2,y2,x3,y3):
    c=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    return c>0

def convex_hull(positions):
    convex = []
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(*p1, *p2, *p3):
                break
            convex.pop()
        convex.append(p3)

    return convex


def rotate_to_starting_point(points):
    start_point = max(points, key=lambda p: (p[1], -p[0]))
    start_index = points.index(start_point)
    return points[start_index:] + points[:start_index]

for points in test_cases:
    points.sort(key=lambda x: (x[1], x[0]))
    upper_hull = convex_hull(points)
    lower_hull = convex_hull(points[::-1])

    # Combine upper and lower hulls and remove duplicates
    full_hull = list(dict.fromkeys(upper_hull + lower_hull))

    # Rotate to start from the point with largest y (smallest x in case of ties)
    full_hull = rotate_to_starting_point(full_hull)

    # Reverse to get clockwise order (except for the first point)
    full_hull = [full_hull[0]] + list(reversed(full_hull[1:]))

    # Output
    print(len(full_hull))
    for point in full_hull:
        print(point[0], point[1])

