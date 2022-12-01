from scripts.open_input import stream_file


def part1():
    max_val = 0
    val = 0
    for line in stream_file(1):
        if line:
            val += int(line)
        else:
            max_val = max(val, max_val)
            val = 0
    return max_val


def part2():
    max_val = [0] * 3
    val = 0
    for line in stream_file(1):
        if line:
            val += int(line)
        else:
            max_val[0] = max(val, max_val[0])
            max_val.sort()
            val = 0
    return sum(max_val)

