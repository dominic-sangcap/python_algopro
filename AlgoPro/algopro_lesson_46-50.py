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