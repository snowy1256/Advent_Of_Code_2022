"""
Lib for AoC22 Convenience functions
"""


def pretty_input(lines):
    pretty_lines = []
    for line in lines:
        line = line.strip("\n")
        pretty_lines.append(line)
    return pretty_lines


def load_input(input_path="input.txt"):
    lines = []
    with open(input_path, "r") as f:
        # Unsure if the file will close if I just return from inside the with
        lines = f.readlines()
    return pretty_input(lines)
