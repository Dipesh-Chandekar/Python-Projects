# Lists representing the numbers on the two maps
map1 = [4, 7, 12, 19, 25, 30]
map2 = [5, 7, 19, 20, 25, 40]

# Convert the lists to sets and find the intersection
treasure_coordinates = set(map1).intersection(set(map2))

print("Treasure Coordinates:", treasure_coordinates)
