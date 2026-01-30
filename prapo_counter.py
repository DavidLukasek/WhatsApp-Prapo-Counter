import sys

import prapo_utils.prapo_file_reader as PrapoReader
import prapo_utils.prapo_message_filter as PrapoFilter
import prapo_utils.prapo_data_handler as PrapoHandler

file_path = "data/prapo.txt"

#checking the number of arguments
if len(sys.argv) < 3:
    print("Error: Too few arguments!")
    print("Usage: python prapo_counter.py <filter message> <mode> [filepath to data]")
    sys.exit(69)

#reading the file, default if not specified
if len(sys.argv) == 4:
    file_path = sys.argv[3]
messages = PrapoReader.read_file_lines(file_path)

#filtering the messages
filterCode = sys.argv[1]
filteredMessages = PrapoFilter.filterMessages(messages, filterCode)

#handling the data based on the given mode code
mode = (int)(sys.argv[2])
PrapoHandler.handle_data(filteredMessages, mode)
