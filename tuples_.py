
my_tuple = (2, 4, 5, 6)
my_tuple2 = tuple([1, 4, 6])
singleton_tuple = (2,)


player_respawn_coordinates = (0, 0, 0)
# player_respawn_coordinates[2] = 200 # won't be able to change

WINDOW_DIMENSIONS = (1240, 1080)


rep_tup = my_tuple * 3
concat = my_tuple + my_tuple2
# print(rep_tup)
# print(concat)
# print(concat[2])


x, y, z = player_respawn_coordinates

# nested typles can also be unpacked
name, (house_no, street) = ("George", (100, 'AX STR'))
# print(x, y, z)
# print(name, house_no, street)


# after 1st 2 values remaining values are returned in rest (list type)
a, b, *rest = (1, 2, "aa", "bb", "cc")
print(a, b)
print(rest)


# methods

# to get index of an element
# gives error if element not in typle
height_idx = player_respawn_coordinates.index(0)
print(height_idx)

# To get frequency of an element in typle
print(rep_tup.count(2))
