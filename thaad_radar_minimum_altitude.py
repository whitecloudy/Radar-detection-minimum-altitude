import math

earth_radius = 6378137
earth_circumference = 2 * earth_radius * math.pi

distance = float(input("Distance(km) : "))*1000   #distance that user input(insert in km)
angle = float(input("Angle(°) : "))     #angle of radar

alpha = (distance/earth_circumference)*2*math.pi   #calculate angle of fan shape

sec_alpha = 1/math.cos(alpha)
if angle!=0:    #When angle is not zero
    cot_theta = (1/math.tan(math.radians(angle)))
    tan_alpha = math.tan(alpha)
    length = (cot_theta*earth_radius*sec_alpha)/(cot_theta-tan_alpha)   #length from center of the earth to point of minimum height
else :  #When angle is zero
    length = sec_alpha * earth_radius

altitude = length - earth_radius  #altitude from the ground

print("Minimum Altitude : {0:.2f}m".format(altitude))

input() #prevent quiting
