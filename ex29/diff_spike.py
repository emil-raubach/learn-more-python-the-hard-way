import difflib
import sys


def main(file_a, file_b, outfile):
    
    with open(file_a, 'r') as a, open(file_b, 'r') as b:
        a_data = a.readlines()
        b_data = b.readlines()

    diff = difflib.ndiff(a_data, b_data)
    outfile.writelines(diff)
    
    # outfile = '\n'.join(diff)
    # sys.stdout.writelines(outfile)
   

if __name__ == "__main__":
    file_A, file_B = sys.argv[1:]
    main(file_A, file_B, sys.stdout)