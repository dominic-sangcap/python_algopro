#Lesson 46
#Angles of a Clock
def calcAngle(h, m):
    hour_angle = (360 / (12 * 60.0)) * (h * 60 + m)
    min_angle = 360 / 60.0 * m
    angle = abs(hour_angle - min_angle)
    angle = min(angle, 360 - angle)
    return angle

#test input 
print(calcAngle(3, 15))
print(calcAngle(3, 00))

#Lesson 47
#climbing stairs
#recursive implementation
def staircase(n):
    if n <= 1:
        return 1
    return staircase(n - 1) + staircase(n - 2)

def staircase2(n):
    prev = 1
    prevprev = 1
    curr = 0
    for i in range(2, n + 1):
        curr = prev + prevprev

        prevprev = prev
        prev = curr
    return curr

#test input
print(staircase2(5))

print(staircase(5))