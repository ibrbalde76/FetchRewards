import sys


# this functions put the lines
# of the text file into a list
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        return data
    except IOError:
        print("Imposssibility to read the file", file)
        sys.exit()
