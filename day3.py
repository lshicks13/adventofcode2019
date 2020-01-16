#Read in the directions from the file and separate them into 2 paths
def get_paths(txtfile):
    with open(txtfile) as f:
        f = f.read().splitlines()
        path1 = f[0].split(',')
        path2 = f[1].split(',')
    return path1, path2

# Get all the points from the given paths
def get_points(path):
    step = 1
    i = j = k = 0
    points = {}
    while i < len(path):
        x = y = 0
        direction = path[i][:1]
        distance = int(path[i][1:])
        if direction == 'R':
            x = 1
        elif direction == 'L':
            x = -1
        elif direction == 'U':
            y = 1
        elif direction == 'D':
            y = -1
        for _ in range(distance):
            j += x
            k += y
            points[step] = (j,k)
            step += 1
        i += 1
    return points

# Get the shared points from the paths
def get_intersections(pts1, pts2):
    sh_pts = {}
    for a in pts1:
        for b in pts2:
            if pts1[a] == pts2[b]:
                sh_pts[a] = pts1[a]
    sh_pts = list(sh_pts.values())
    return sh_pts

# Get the manhattan distance for each of the shared points
# and return the shortest distance
def manhattan_distance(pts):
    i = 0
    mdist = {}
    while i < len(pts):
        mdist[i] = abs(0 - int(pts[i][0])) + abs(0 - int(pts[i][1]))
        i += 1
    smd = list(mdist.values())
    md = min(smd)
    return md

def main():
    path1, path2 = get_paths('paths2.txt')
    pts1 = get_points(path1)
    pts2 = get_points(path2)
    inter = get_intersections(pts1,pts2)
    print('Intersecting Points:\n', inter)
    print('Manhattan Distance:\n', manhattan_distance(inter))

main()