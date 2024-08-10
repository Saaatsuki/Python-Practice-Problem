def find_fourth_point(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    for x in x_coords:
        if x_coords.count(x) == 1:
            fourth_x = x
            break

    for y in y_coords:
        if y_coords.count(y) == 1:
            fourth_y = y
            break


    print(f"{fourth_x} {fourth_y}")


num1,num2 = map(int,input().split())
num3,num4 = map(int,input().split())
num5,num6 = map(int,input().split())

points = [(num1, num2), (num3, num4), (num5, num6)]

find_fourth_point(points)
