input = open("second\input.txt", "r")
lines = input.readlines()
#task 1
def get_shape_points(shape):
    if shape == "X" or shape == "A":
        return 1
    if shape == "Y" or shape == "B":
        return 2
    if shape == "Z" or shape == "C":
        return 3

def get_match_result(their, mine):
    theirShapePoint = get_shape_points(their)
    mineShapePoint = get_shape_points(mine)
    if theirShapePoint == mineShapePoint:
        return 3
    if theirShapePoint == 1:
        if mineShapePoint == 2:
            return 6
        if mineShapePoint == 3:
            return 0
    if theirShapePoint == 2:
        if mineShapePoint == 1:
            return 0
        if mineShapePoint == 3:
            return 6
    if theirShapePoint == 3:
        if mineShapePoint == 1:
            return 6
        if mineShapePoint == 2:
            return 0

score = 0
for line in lines:
    shapes = line.split(" ")
    their = shapes[0].strip()
    mine = shapes[1].strip()
    score += get_shape_points(mine)
    score += get_match_result(their, mine)

#print(score)
#task2

def get_win(theirShapePoint):
    shapeNumber = 0
    if theirShapePoint == 1:
        shapeNumber = get_shape_points("Y")
    elif theirShapePoint == 2:
        shapeNumber = get_shape_points("Z")
    elif theirShapePoint == 3:    
        shapeNumber = get_shape_points("X")
    
    return 6 + shapeNumber

def get_draw(theirShapePoint):
    shapeNumber = theirShapePoint

    return 3 + shapeNumber

def get_loss(theirShapePoint):
    shapeNumber = 0
    if theirShapePoint == 1:
        shapeNumber = get_shape_points("Z")
    elif theirShapePoint == 2:
        shapeNumber = get_shape_points("X")
    elif theirShapePoint == 3:    
        shapeNumber = get_shape_points("Y")
    return 0 + shapeNumber

def get_match_result(theirShapePoint, mine):
    if mine == "X":
        return get_loss(theirShapePoint)
    if mine == "Y":
        return get_draw(theirShapePoint)
    if mine == "Z":
        return get_win(theirShapePoint)

score = 0
for line in lines:
    shapes = line.split(" ")
    their = shapes[0].strip()
    mine = shapes[1].strip()
    theirShapePoint = get_shape_points(their)
    score += get_match_result(theirShapePoint, mine)

print(score)