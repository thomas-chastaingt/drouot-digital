import itertools

coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

def counting_rectangles(coordinates):
    number_of_rectangles = 0
    for (a, b, c, d) in itertools.combinations(coordinates, 4):
        if a[0] == b[0] and c[0] == d[0] and a[1] == c[1] and b[1] == d[1]:
                number_of_rectangles += 1
    print(number_of_rectangles)

    
counting_rectangles(coordinates)

