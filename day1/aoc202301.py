import pathlib
import sys
from functools import reduce

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.split()

def findCalibrationValue(string, includeWords):

    indices = []

    numbers = []

    # Index of integer matches the word
    integers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for number in integers:

        word = number

        index = integers.index(number)

        indexOfInteger = string.find(str(index))

        while indexOfInteger >= 0:
        
            indices.append(indexOfInteger)

            numbers.append(index)

            indexOfInteger = string.find(str(index), indexOfInteger + 1)

        if includeWords == True:
            
            indexOfWord = string.find(word)

            while indexOfWord >= 0:

                indices.append(indexOfWord)

                numbers.append(index)

                indexOfWord = string.find(word, indexOfWord + 1)
    
    firstDigit = str(numbers[indices.index(min(indices))])

    lastDigit = str(numbers[indices.index(max(indices))])

    calibrationValue = int(''.join((firstDigit, lastDigit)))

    return calibrationValue

def findCalibrationValuesSum(data, includeWords = False):
    
    calibrationValues = []

    for line in data:

        calibrationValues.append(findCalibrationValue(line, includeWords))

    return reduce(lambda a, b: a + b, calibrationValues)

def part1(data):
    """Solve part 1."""
    
    return findCalibrationValuesSum(data, False)

def part2(data):
    """Solve part 2."""
    
    return findCalibrationValuesSum(data, True)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""

    data = parse(puzzle_input)

    solution1 = part1(data)

    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        
        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)

        print("\n".join(str(solution) for solution in solutions))