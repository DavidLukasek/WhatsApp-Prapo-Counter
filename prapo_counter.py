import sys

import prapo_utils.prapo_file_reader as PrapoReader
import prapo_utils.prapo_message_filter as PrapoFilter


#checking the number of arguments
if len(sys.argv) < 4:
    print("Error: Too few arguments!")
    print("Usage: python prapo_counter.py <file_path> <filter_code> <mode>")
    sys.exit(69)

#reading the file
file_path = sys.argv[1]
messages = PrapoReader.read_file_lines(file_path)

#filtering the messages
filterCode = sys.argv[2]
filteredMessages = PrapoFilter.filterMessages(messages, filterCode)
