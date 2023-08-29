def div_by_three(x):
    sum = x/3
    print(sum)
    return sum == int(sum)


def max2(x,y):
    if x>y:
        return x
    else: 
        return y

def max3(x,y,z):
    stor = max2(x,y)
    störst = max2(stor,z)
    return störst

n = max3(67, 67, 67)
print(n)
