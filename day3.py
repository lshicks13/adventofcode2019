#Read in the directions from the file and separate them into 2 paths
def get_paths(txtfile):
    with open(txtfile) as f:
        f = f.read().splitlines()
        path1 = f[0].split(',')
        path2 = f[1].split(',')
    
    return path1, path2

def get_direction(path):
    steps = i = j = x = y = 0
    points = {}
    while i < len(path):
        direction = path[i][:1]
        distance = int(path[i][1:])
        steps += distance
        #print('this is the direction\n', direction, '\nthis is the distance\n', distance)
        if direction == 'R':
            #print(x,'this is x before adding distance')
            #r = x + distance * 1
            print(x,'this is x before for')
            distance = distance * 1 + 1
            while x < distance:
            # for a in range(x,distance):
                 
                 points[j] = (x,y)
                 x += 1
                 j += 1
            
            #points = get_points_along_path(x,r + 1)
        elif direction == 'L':
            #x = x + distance * -1
            distance = distance * -1 + 1
            while x > 
            # for a in range(x,distance):
            #     x = a
            #     points[j] = (x,y)
            #     j += 1
        elif direction == 'U':
            y = y + distance * 1
        elif direction == 'D':
            #y = y + distance * -1
            distance = distance * -1 + 1
            # for b in range(y,distance):
            #     y = b
            #     points[j] = (x,y)
            #     j += 1
        #for a in range():
        # pts[a] = (x,y)
        # print(a,'in get points')
        #points[i] = (x,y)
        i += 1

    return points, steps

def get_points_along_path(start, stop):
    x = start[0]
    y = start[1]
    pts = {}
    for a in range(start, stop):
        pts[a] = (x,y)
        print(a,'in get points')
    return pts
    

path1, path2 = get_paths('path2.txt')

pts1, stps1 = get_direction(path1)
pts2, stps2 = get_direction(path2)
print('Path 1 Points ', pts1, '\n Path 1 Steps: ', stps1)
# print('Path 2 Points ', pts2, '\n Path 2 Steps: ', stps2)