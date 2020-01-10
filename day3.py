#Read in the directions from the file and separate them into 2 paths
def get_paths(txtfile):
    with open(txtfile) as f:
        f = f.read().splitlines()
        path1 = f[0].split(',')
        path2 = f[1].split(',')
    
    return path1, path2

def get_direction(path):
    # step = 0
    # i = 0
    # while i < len(path):
    direction = path[i][:1]
    distance = path[i][1:]
        #print('this is the direction\n', direction, '\nthis is the distance\n', distance)
    if direction == 'R':
        x = 1
    if direction == 'L':
        x = -1
    if direction == 'U':
        y = 1
    if direction == 'D':
        y = -1
        #i += 1

def move()
path1, path2 = get_paths('paths.txt')
print(get_direction(path1))