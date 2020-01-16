#Read in the directions from the file and separate them into 2 paths
def get_paths(txtfile):
    with open(txtfile) as f:
        f = f.read().splitlines()
        path1 = f[0].split(',')
        path2 = f[1].split(',')
    
    return path1, path2

def get_points(path):
    step = 1
    j = k = 0
    i = 0
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
        #print('this is the distance\n', distance)
        for _ in range(distance):
            # print('this is the distance\n', distance)
            # print('this is x\n', x)
            # print('this is y\n', y)
            j += x
            k += y
            # print('this is j\n', j)
            # print('this is k\n', k)
            # print('this is step before\n', step)
            points[step] = (j,k)
            #print('these are the points\n', points)
            step += 1
            #print('this is step after\n', step)
        i += 1
    return points

def get_intersections(pts1, pts2):
    #k = 1
    sh_pts = {}
    #result = {}
    #while k < len(pts1) or k < len(pts2):
    for a in pts1:
        for b in pts2:
            if pts1[a] == pts2[b]:
                sh_pts[a] = pts1[a]
    sh_pts = list(sh_pts.values())
                    #sh_pts[k + 1] = pts2[b]
                    #print('these are shared pts at positions\n', a, b)
        # if pts1[k] == pts2[k]:
        #     print('this is a shared pt\n', pts1[k], pts2[k])
        #shared_items = {k: pts1[k] for k in pts1 if k in pts2 and pts1[k] == pts2[k]}
        #print(len(shared_items))
        #k += 1
    
    # for key,value in sh_pts.items():
    #     #print('sh pts key\n', key) 
    #     #print('sh pts value\n',value)

    #     if value in result.values():
    #         break
    #     else:
    #         result[key] = value
    #         #print('sh pts values\n',sh_pts.values())
    # #print('this is sh pts\n', sh_pts)
    # ls_pts = list(result.values())
    # #print('this is the result\n', ls_pts[0][0])

    return sh_pts #a, pts1[a], b, pts2[b]  

def manhattan_distance(pts):
    i = 0
    mdist = {}
    while i < len(pts):
        # print('')
        # print('this is i in while\n', i)
        # print('this is x\n', pts[i][0], '\nthis is y\n', pts[i][1])
        mdist[i] = abs(0 - int(pts[i][0])) + abs(0 - int(pts[i][1]))
        i += 1
        #print('this is i in while after\n', i)
    smd = list(mdist.values())
    md = min(smd)
    return md
    
      

    # if num1 < num2:
    #     return pos1
    # elif num2 < num1:
    #     return pos2
    # else:
        # return num1


path1, path2 = get_paths('paths.txt')
pts1 = get_points(path1)
pts2 = get_points(path2)
# print('Path 1 pts\n', pts1)
# print('Path 2 pts\n', pts2)
# print('Path 1 pt\n', pts1[1])
inter = get_intersections(pts1,pts2)
print('this is intersecting pts\n', inter)
#print('Path1 step and shared pt\n', step1, spt1,'\nPath2 step and shared pt\n', step2, spt2)
# pos = get_least_steps(step1, step2, spt1, spt2)
# ans = get_md(pos)
# print('this is the final md\n', ans)
print(manhattan_distance(inter))
#print(sum(abs(a-b) for a,b in zip(pts1,pts2)))