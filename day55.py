# 03 - May - 2020

# Angles of a Clock

# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

def calcAngle(h, m):
    # Fill this in.
    if h == 12:
        h = 0
    if m == 60:
        h += 1
        m = 0
    hour_angle = int(h * 30 + m * 0.5)
    minute_angle = int(m * 6)
    return min(abs(hour_angle - minute_angle), abs(360 - hour_angle + minute_angle))

print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165