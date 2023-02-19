# This is a test of the touch & echo commands
print(f"INSERT INTO cardgame_card (number, point_value, suit, collection_id) VALUES")
for i in range(1, 105):
    point_value = 1
    if i == 55:
        point_value = 7
    elif i % 11 == 0:
        point_value = 5
    elif i % 10 == 0:
        point_value = 3
    elif i % 5 == 0:
        point_value = 2
    print(f"({i}, {point_value}, '', NULL),")
