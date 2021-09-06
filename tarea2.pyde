q = 0
w = 0
v = 0
def setup ():
    size (300, 300)
def draw():
    background(0)
    global q
    global w
    global v
    square(3, q, 50)
    if q > height:
       q = 0
    else:
       q = map(second(), 0, 59, 0, height)
    square(100, w, 60)
    if w > height:
       w = 0
    else:
       w = map(minute(), 0, 59, 0, height)
    square(222, v, 70)
    if v > height:
       v = 0
    else:
       v = map(hour(), 0, 59, 0, height)
