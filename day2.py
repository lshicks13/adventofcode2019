import operator

# Open file and create a list of integers
def clst2arr(tfile):
    with open(tfile) as f:
        f = f.read()
        clist = f.split(',')
        cl = []

        for i in clist:
            i = int(i)
            cl.append(i)
    
    return cl

#
def intcodepart1(array):
    operatorlookup = {

        '+': operator.add,

        '*': operator.mul,

    }

    i = 0

    while i < len(array):

        if array[i] == 1:

            op = operatorlookup.get('+')

        elif array[i] == 2:

            op = operatorlookup.get('*')

        elif array[i] == 99:

            break

        result = op(array[array[i + 1]], array[array[i + 2]])

        array[array[i + 3]] = result
      
        i += 4


    return array[0], array[1], array[2]

# Create the noun and verb pairs
def pairs_range(limit1, limit2):
    
    for i1 in range(limit1):
        for i2 in range(limit2):
            yield i1, i2

def change_inputs(textfile, exout, limit1, limit2):
    for x, y in pairs_range(limit1, limit2):
        lst = clst2arr(textfile)

        lst[1] = y

        lst[2] = x

        result, noun, verb = intcodepart1(lst)

        if exout == result:
            solution = 100 * noun + verb
            return "Solution ", solution


print(change_inputs('list.txt', 19690720, 100, 100))