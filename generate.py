import sys

template = """import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "#INPUT_FILE_NAME#"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

part_one = None
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")

"""


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("Day number if not given. Example python generate.py day03")

    day = sys.argv[1]
    input_filename = f"./inputs/{day}.txt"
    input_file = open(input_filename, "w")
    input_file.close()

    with open(f"{day}.py", "w") as python_file:
        python_file.write(template.replace("#INPUT_FILE_NAME#", input_filename))