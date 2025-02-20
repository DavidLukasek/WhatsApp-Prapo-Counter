import sys

import prapo_utils.prapo_file_reader as PrapoReader

#checking the number of arguments
if len(sys.argv) < 2:
    print("Error: Too few arguments!\nUsage: python prapo_counter.py <file_path>")
    sys.exit(1)

#reading the file
file_path = sys.argv[1]
messages = PrapoReader.read_file_lines(file_path)
