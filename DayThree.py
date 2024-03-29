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

def getDistanceBetweenNodes(node_a, node_b):
    delta_pos = np.array(np.array(node_b) - np.array(node_a)).tolist()
    delta_pos_sum = np.sum(delta_pos)
    delta_pos_sum_abs = abs(int(delta_pos_sum))
    return delta_pos_sum_abs

def getStepsToIntersections(line_nodes_a, line_nodes_b, intersections):
    for intersection in intersections:
        line_done_a = False
        line_done_b = False
        line_steps_a = 0
        line_steps_b = 0

        # This don't work because the intersections is not at the same position as the nodes.

        for i in range(1, len(line_nodes_a)):
            if line_done_a == False:
                pos_a = line_nodes_a[i]
                line_steps_a += getDistanceBetweenNodes(pos_a, line_nodes_a[i-1])
                if pos_a == intersection:
                    line_done_a = True

            if line_done_b == False:
                pos_b = line_nodes_b[i]
                line_steps_b += getDistanceBetweenNodes(pos_b, line_nodes_b[i-1])
                if pos_b == intersection:
                    line_done_b = True

            continue

        total_steps = line_steps_a + line_steps_b

        continue

    return 0 

def testPartTwo(test_inputs):
    for test_input in test_inputs:
        line_nodes_a = getLineNodes(test_input[0][0])
        line_nodes_b = getLineNodes(test_input[0][1])

        intersections = getLineSegmentIntersections(line_nodes_a, line_nodes_b)
        steps = getStepsToIntersections(line_nodes_a, line_nodes_b, intersections)

        continue

    return 0

def partTwo():
    input_file = 'DayThreeInput.txt'
    test_input = [[[['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']], 30],
                    [[['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']], 610],
                    [[['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']], 410]]
    data = getData(input_file)
    testPartTwo(test_input)


    return 0

if __name__ == '__main__':
    # partOne()
    partTwo()