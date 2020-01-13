def get_points(point1,point2):
    i = 0
    points = {}
    print(point1, 'point1')
    m = (point1[1]-point2[1])/(point1[0]-point2[0])
    b = (point1[0]*point2[1] - point2[0]*point1[1])/(point1[0]-point2[0])
    while i < point2[0]:
        y = m * i + b
        x = i
        points[i] = (x,y)
        i += 1
    return points

#Read in the directions from the file and separate them into 2 paths
def get_paths(txtfile):
    with open(txtfile) as f:
        f = f.read().splitlines()
        path1 = f[0].split(',')
        path2 = f[1].split(',')
    
    return path1, path2

def get_direction(path):
    step = 1
    i = j = k = 0
    points = {}
    while i < len(path):
        x = y = 0
        direction = path[i][:1]
        distance = int(path[i][1:])
        #steps += distance
        #print('this is the direction\n', direction, '\nthis is the distance\n', distance)
        if direction == 'R':
            x = 1
        elif direction == 'L':
            x = -1
        elif direction == 'U':
            y = 1
        elif direction == 'D':
            y = -1
        for _ in range(distance):
            print(distance, 'this is the distance')
            print(x, 'this is x')
            print(y, 'this is y')
            j += x
            k += y
            print(j, 'this is j')
            print(k, 'this is k')
            print(step, '\nthis is step before')
            points[(j, k)] = step
            print(points, '\nthese are the points')
            step += 1
            print(step, '\nthis is step after')
        i += 1

    return points#, step

path1, path2 = get_paths('path2.txt')
print(get_direction(path1))