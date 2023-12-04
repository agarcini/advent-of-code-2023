import pathlib
import sys
from functools import reduce

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.split()

def part1(data):
    """Solve part 1."""

    def replaceNumberWords(line):
        
        line = line.replace('one', 'o1e')
        line = line.replace('two', 't2o')
        line = line.replace('three', 't3e')
        line = line.replace('four', 'f4r')
        line = line.replace('five', 'f5e')
        line = line.replace('six', 's6x')
        line = line.replace('seven', 's7n')
        line = line.replace('eight', 'e8t')
        line = line.replace('nine', 'n9e')

        return line

    def findCalibrationValue(string):

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

            indexOfWord = string.find(word)

            while indexOfWord >= 0:

                indices.append(indexOfWord)

                numbers.append(index)

                indexOfWord = string.find(str(index), indexOfWord + 1)
        
        firstDigit = str(numbers[indices.index(min(indices))])

        lastDigit = str(numbers[indices.index(max(indices))])

        calibrationValue = int(''.join((firstDigit, lastDigit)))

        return calibrationValue
    
    calibrationValues = []

    for line in data:

        calibrationValues.append(findCalibrationValue(replaceNumberWords(line)))

    print(calibrationValues)

    return reduce(lambda a, b: a + b, calibrationValues)

def part2(data):
    """Solve part 2."""

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