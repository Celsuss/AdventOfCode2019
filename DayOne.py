import math

def test(test_input, function):
    for key in test_input:
        input = key
        output_ref = test_input[key]
        output = function(input)
        assert output == output_ref

def getInputData(path):
    file = open(path, 'r')
    return file.readlines()

def main():
    input_file = 'DayOneInput.txt'
    test_input = {12:2, 14:2, 1969:654, 100756:33583}
    function = lambda x: math.floor(x/3)-2

    test(test_input, function)
    data = getInputData(input_file)

    return 0

if __name__ == '__main__':
    main()