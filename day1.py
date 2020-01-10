def total_fuel(txtfile):
    with open(txtfile) as f:
        z = 0 
        for x in f:
            y = fuel_req(x)
            z = z + y
            while y > 5:
                fr = fuel_req(y)
                z = z + fr
                y = fr
    return z

def fuel_req(num):
    x = int(num)
    y = int(x / 3) - 2
    return y

print(total_fuel('entries.txt'))


