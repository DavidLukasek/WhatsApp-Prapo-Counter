import sys

import prapo_utils.prapo_file_reader as PrapoReader
import prapo_utils.prapo_message_filter as PrapoFilter
import prapo_utils.prapo_data_handler as PrapoHandler

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

#handling the data based on the given mode code
mode = (int)(sys.argv[3])
PrapoHandler.handle_data(filteredMessages, mode)
