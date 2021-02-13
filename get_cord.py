
def get_y(t1,t2,x):
    s = get_slope(t1,t2)
    c = t1[1] - s * t1[0]
    y = s * x + c
    return int(y)

def get_slope(t1,t2):
    slope = (t1[1]-t2[1])/(t1[0]-t2[0])
    return slope

print(get_y((1,3),(4,9),3))
