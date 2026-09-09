hour=int(input())
minute=int(input())
hour_angle=(hour%12)*30+minute*0.5
minute_angle=minute*6
angle=abs(hour_angle-minute_angle)
print(min(angle,360-angle))
