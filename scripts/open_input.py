from pathlib import Path


def stream_file(day):
    with open((Path(__file__).parent / f'../inputs/AoC2022-{str(day).zfill(2)}').resolve(), 'r') as file:
        for line in file:
            line = line.strip()
            yield line

def read_file(day):
    with open((Path(__file__).parent / f'../inputs/AoC2022-{str(day).zfill(2)}').resolve(), 'r') as file:
        return file.read()
