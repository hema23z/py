areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
areas[-1]=10.50
areas[4]= "chill zone"

areas_1 =areas + ["poolhouse", 24.5]

areas_2 =areas_1 + ["garage", 15.45]

del areas[10:12]

print (areas)


are = [11.25, 18.0, 20.0, 10.75, 9.50]


are_copy = are[:]

are_copy[0] = 5.0

print(are)
print(are_copy)