areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

print(areas[1])

print(areas[-1])

print(areas[5])

downstairs = areas[:6]

upstairs = areas[6:]

print (downstairs)
print (upstairs)
#************************************
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

print(house[4][1])