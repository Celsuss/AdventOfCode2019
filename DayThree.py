import numpy as np
import math
import sys

def getDirectionAndLength(move):
    direction = [0,0]
    if move[0] == 'R':
        direction = [1,0]
    elif move[0] == 'D':
        direction = [0,-1]
    elif move[0] == 'L':
        direction = [-1,0]
    elif move[0] == 'U':
        direction = [0,1]

    length = int(move[1:])

    return direction, length

def getLineIntersection(point_a_1, point_a_2, point_b_1, point_b_2):
    line1 = (point_a_1, point_a_2)
    line2 = (point_b_1, point_b_2)
    x_delta = (point_a_1[0] - point_a_2[0], point_b_1[0] - point_b_2[0])
    y_delta = (point_a_1[1] - point_a_2[1], point_b_1[1] - point_b_2[1])

    det = lambda a, b : a[0] * b[1] - a[1] * b[0]
    div = det(x_delta, y_delta)

    if div == 0:
        # No intersection
        return 0, 0

    d = (det(*line1), det(*line2))
    x = det(d, x_delta) / div
    y = det(d, y_delta) / div

    # Calculate if it's inside segment
    r_x_a = (x - point_a_1[0]) / ((point_a_2[0] - point_a_1[0]) if (point_a_2[0] - point_a_1[0]) != 0 else 1)
    r_y_a = (y - point_a_1[1]) / ((point_a_2[1] - point_a_1[1]) if (point_a_2[1] - point_a_1[1]) != 0 else 1)
    r_x_b = (x - point_b_1[0]) / ((point_b_2[0] - point_b_1[0]) if (point_b_2[0] - point_b_1[0]) != 0 else 1)
    r_y_b = (y - point_b_1[1]) / ((point_b_2[1] - point_b_1[1]) if (point_b_2[1] - point_b_1[1]) != 0 else 1)

    # Make sure the lines intersect inside the line segment.
    if (r_x_a >= 0 and r_x_a <= 1) and (r_y_a >= 0 and r_y_a <= 1) and (r_x_b >= 0 and r_x_b <= 1) and (r_y_b >= 0 and r_y_b <= 1):
        return x, y
    else:
        # Intersection outside of line segment.
        return 0, 0

    return x, y



# def getLineIntersection2(point_a_1, point_a_2, point_b_1, point_b_2):
#     line_a_x = point_a_2[0] - point_a_1[0]
#     line_a_y = point_a_2[1] - point_a_1[1]
#     c_a = line_a_x * point_a_1[0] + line_a_y * point_a_2[1]

#     line_b_x = point_b_2[0] - point_b_1[0]
#     line_b_y = point_b_2[1] - point_b_1[1]
#     c_b = line_b_x * point_b_1[0] + line_b_y * point_b_2[1]
    
#     denominator = line_a_x * line_b_y - line_b_x * line_a_y
#     if denominator == 0:
#         # No intersection
#         return 0, 0

#     intersection_x = (line_b_y * c_a - line_a_y * c_b) / denominator
#     intersection_y = (line_a_y * c_b - line_b_y * c_a) / denominator
#     r_x_a = (intersection_x - point_a_1[0]) / (point_a_2[0] - point_a_1[0])
#     r_y_a = (intersection_y - point_a_1[1]) / (point_a_2[1] - point_a_1[1])

#     if (r_x_a <= 0 or r_x_a >= 1) and (r_y_a <= 0 or r_y_a >= 1):
#         return intersection_x, intersection_y
#     else:
#         return 0, 0

def getLineNodes(moves):
    nodes = []
    pos = np.array([0,0])
    for move in moves:
        direction, length = getDirectionAndLength(move)
        pos = pos + (np.array(direction) * length)
        nodes.append([pos[0], pos[1]])

    return nodes

def getDistance(point):
    return int(abs(point[0]) + abs(point[1]))

def getIntersectionDistances(intersections):
    distances = []
    for intersection in intersections:
        distance = getDistance(intersection)
        distances.append(distance)
    return distances

def getShortestIntersectionDistance(intersections):
    shortest_distance = sys.maxsize
    for intersection in intersections:
        distance = getDistance(intersection)
        if distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance

def getLineSegmentIntersections(line_one_nodes, line_two_nodes):
    intersections = []

    for i in range(len(line_one_nodes)-1):
        for j in range(len(line_two_nodes)-1):
            intersection_x, intersection_y = getLineIntersection(line_one_nodes[i], line_one_nodes[i+1],
                                                                line_two_nodes[j], line_two_nodes[j+1])
            if intersection_x != 0 and intersection_y != 0:
                intersections.append((intersection_x, intersection_y))

    return intersections

def testPartOne(test_inputs):
    test_count = 1
    for test_input in test_inputs:
        line_one_nodes = getLineNodes(test_input[0][0])
        line_two_nodes = getLineNodes(test_input[0][1])

        intersections = getLineSegmentIntersections(line_one_nodes, line_two_nodes)
        distances = getIntersectionDistances(intersections)
        intersection_distance = getShortestIntersectionDistance(intersections)

        assert(intersection_distance == test_input[1])
        print('[Success] Test {}/{}'.format(test_count, len(test_inputs)))
        test_count += 1

def getData(file):
    file = open(file, 'r')

    lines = file.readlines()
    lines[0] = lines[0].strip('\n')
    lines[1] = lines[1].strip('\n')
    line_a = lines[0].split(',')
    line_b = lines[1].split(',')
    return [line_a, line_b]

def partOne():
    input_file = 'DayThreeInput.txt'
    test_input = [[[['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']], 6],
                    [[['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']], 159],
                    [[['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']], 135]]
    data = getData(input_file)

    testPartOne(test_input)
    line_one_nodes = getLineNodes(data[0])
    line_two_nodes = getLineNodes(data[1])

    intersections = getLineSegmentIntersections(line_one_nodes, line_two_nodes)
    distances = getIntersectionDistances(intersections)
    intersection_distance = getShortestIntersectionDistance(intersections)

    return 0

if __name__ == '__main__':
    partOne()