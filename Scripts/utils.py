def read_file(filename : str, verbose = False):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    if verbose:
        print(f"Read file, print first 10 lines:\n{lines[:10]}")
    return lines

def read_file_as_one(filename : str) -> str:
    with open(filename) as file:
        input = file.read()
    return input