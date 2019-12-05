import numpy as np
import math

def testPartOne(test_input, function):
    for key in test_input:
        input = key
        output_ref = test_input[key]
        output = function(input)
        assert output == output_ref

def getInputData(path):
    file = open(path, 'r')
    lines = file.readlines()
    return [int(i) for i in lines]

def getTotalFuelRequirement(data, function):
    total_fuel = 0
    for row in data:
        total_fuel = total_fuel + function(row)

    return total_fuel

def partOne():
    input_file = 'DayOneInput.txt'
    test_input = {12:2, 14:2, 1969:654, 100756:33583}
    function = lambda x: math.floor(x/3)-2

    testPartOne(test_input, function)
    data = getInputData(input_file)
    total_fuel = getTotalFuelRequirement(data, function)
    print('Part One: Total fuel required is: {}'.format(total_fuel))

    return total_fuel

def partTwoFunction(x):
    y = int(np.clip(math.floor(x/3)-2, a_min=0, a_max=None))
    if y <= 0:
        return y
    else:
        return y + partTwoFunction(y)

def testPartTwo(test_input):
    for key in test_input:
        output_ref = test_input[key]
        output = partTwoFunction(key)
        assert output == output_ref

    return 0

def partTwo():
    input_file = 'DayOneInput.txt'
    total_fuel_for_modules = partOne()
    test_input = {14:2, 1969:966, 100756:50346}

    testPartTwo(test_input)
    data = getInputData(input_file)
    total_fuel = getTotalFuelRequirement(data, partTwoFunction)
    print('Part Two: Total fuel required is: {}'.format(total_fuel))

    return 0

if __name__ == '__main__':
    partOne()
    partTwo()