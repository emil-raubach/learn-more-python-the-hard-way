def print_files(args=None):
    "Print the contents of a file to the stdout"

    outfile = []

    for filename in args[1:]:
        with open(filename) as f:
            outfile.append(f.read())

    return outfile