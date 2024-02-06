################################
#Tshewang Dorji
# Section A
# 02230312
################################
# REFERENCES
# Links that you referred while solving the problem
# https://realpython.com/python-rock-paper-scissors/
# https://codereview.stackexchange.com/questions/231706/python-rock-paper-scissors-via-a-class-to-handle-the-game
################################
# SOLUTION
# Your Solution Score:
# 63335

def read_input(filename="input_2_cap2.txt"):
    # This function reads input from a file and returns the lines as a list
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def parse_line(line):
    # This function parses each line and converts the ranges to a list of lists
    return [list(map(int, range_.split('-'))) for range_ in line.strip().split(', ')]

def count_overlapping_assignments(spaces):
    # This function counts the number of overlapping assignments
    total_overlaps = 0
    for i in range(len(spaces)):
        for j in range(i + 1, len(spaces)):
            if max(spaces[i][0], spaces[j][0]) <= min(spaces[i][1], spaces[j][1]):
                total_overlaps += 1
    return total_overlaps

def task_1(lines):
    # This function performs Task 1: counts the total number of overlapping assignments
    total_people = len(lines) * 2  # Each line corresponds to two people
    total_overlaps = 0

    # Iterate over each line and count overlaps
    for line in lines:
        spaces = parse_line(line)
        total_overlaps += count_overlapping_assignments(spaces)

    # Print the result
    print(f"There were {total_people} people assigned, and there are {total_overlaps} overlapping space assignments")

def count_completely_overlapping_assignments(spaces):
    # This function counts the number of completely overlapping assignments
    total_overlaps = 0
    for i in range(len(spaces)):
        for j in range(i + 1, len(spaces)):
            if spaces[i][0] <= spaces[j][0] and spaces[i][1] >= spaces[j][1]:
                total_overlaps += 1
    return total_overlaps

def task_2(lines):
    # This function performs Task 2: counts the total number of completely overlapping assignments
    total_overlaps = 0

    # Iterate over each line and count completely overlapping assignments
    for line in lines:
        spaces = parse_line(line)
        total_overlaps += count_completely_overlapping_assignments(spaces)

    # Print the result
    print(f"There were {total_overlaps} assignments that overlap completely")

if __name__ == "__main__":
    # Read input from the file
    lines = read_input()
    
    # Perform Task 1
    task_1(lines)
    
    # Perform Task 2
    task_2(lines)


