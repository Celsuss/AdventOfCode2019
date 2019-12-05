
commands = {1:'add', 2:'multiply', 99:'end'}

def getData(file):
    file = open(file, 'r')
    lines = file.readlines()[0].split(',')
    return [int(i) for i in lines]

def add(data, add_pos1, add_pos2, store_pos):
    val_1 = data[add_pos1]
    val_2 = data[add_pos2]
    data[store_pos] = val_1 + val_2
    return data

def multiply(data, multiply_pos1, multiply_pos2, store_pos):
    val_1 = data[multiply_pos1]
    val_2 = data[multiply_pos2]
    data[store_pos] = val_1 * val_2
    return data

def parseInput(input):
    for i in range(0, len(input), 4):
        if input[i] not in commands:
            continue

        if commands[input[i]] == 'add':
            input = add(input, input[i+1], input[i+2], input[i+3])
        elif commands[input[i]] == 'multiply':
            input = multiply(input, input[i+1], input[i+2], input[i+3])
        elif commands[input[i]] == 'end':
            return input

    return input

def testPartOne(test_input):
    for data in test_input:
        input = data[0]
        output_ref = data[1]
        output = parseInput(input)
        assert output == output_ref

    return 0

def partOne():
    input_file = 'DayTwoInput.txt'
    test_input = [[[1,0,0,0,99],[2,0,0,0,99]], [[2,3,0,3,99],[2,3,0,6,99]], [[2,4,4,5,99,0],[2,4,4,5,99,9801]], [[1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99]]]
    data = getData(input_file)

    testPartOne(test_input)
    data[1] = 12
    data[2] = 2
    output = parseInput(data)
    print('Part One output: {}'.format(output[0]))

    return 0

if __name__ == '__main__':
    partOne()


    1,1,1,4,99,5,6,0,99

    1,1,1,4,2