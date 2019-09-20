# create a version of hexdump
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Immitation of the `hexdump` CLI program"
    )

    parser.add_argument(
        'file', type=str, nargs=1, 
        help='The input file to display' 
    )

    parser.add_argument(
        '-C', '--canon', help='Canonical hex+ASCII display'
    )

    return parser.parse_args()

def main(args=None):
    # TODO:  If you give no filename, take input from stdin. 

    # Open the file
    if args.file is not None:
        instream = open(args.file[0])
    else:
        sys.exit(1)

    text_list = []
    # Get the data from the file  
    for line in instream.readlines():
        text_list.append(line)
    instream.close()

    # Convert text to unicode values, and then to hex
    hx = [hex(ord(character)).lstrip('0x') for character in str(text_list)]

    # print(hx)
    # print(text_list)

    # Try some shit like this... make a template to loop over.
    # May be too fancy, but could look into the Jinja2 package.
    # print(
    #       '{0:0>x}  {1}  {2} |{3}|\n'.format(42, 'hexidecimal stuffs', 'more 
    #        hex stuffs', 'ascii stuffs'))
    # Create two variable fed by range object that are in multiples of 8 and 16
    # use these varibles as the start/stop indices for slicing the list of hex 
    # values
    # 
    for i in range(0, len(hx), 16):
        print(
            f"{i:0>8x} ", *hx[i:i + 16])
    

if __name__ == "__main__":
    # sys.exit(main(sys.argv))
    main(parse_arguments())