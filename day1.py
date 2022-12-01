import os


def read_input():
    elves = []
    path = "input.txt"
    with open(path, "r") as f:
        lines = f.readlines()
        elf = []
        for line in lines:
            if len(line) > 2:
                line = line.strip("\n")
                elf.append(int(line))
            else:
                elves.append(elf)
                elf = []
    return elves


if __name__ == "__main__":
    elves = read_input()
    elf_calories = []
    for elf in elves:
        total_calories = sum(elf)
        elf_calories.append(total_calories)

    elf_calories.sort()
    print(sum(elf_calories[-3:]))
