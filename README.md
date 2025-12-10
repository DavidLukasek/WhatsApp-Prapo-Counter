# WhatsApp Prapo Counter
## Project info
This 11/10 gem of a script offers calculating how many Prapos any user has by counting how many messages contain a given literal string by abusing the WhatsApp chat exporting function.

I'm so so sorry it is made in Python...
## Running the program
The starting point of the program is the [prapo_counter.py](prapo_counter.py) module located in the root of the project.

The program is called with 3 parameters in this order:
  *  String containing the path to the source data file
  *  String containing the filtering code to search for in the data
  *  int representing the mode in which to interpret the data
#### For example, to check how many messages does David have in Prapo, call:
python3 prapo_counter.py <your_path_to_the_file> David 1
## Implemented codes/expandability
Currently implemented modes are:
 * 1 - prints number of messages containing the filtering code on the std output
 * 2 - prints all the messages counted above, each on its own line, on the std output

Possible additions in the future may include:
 * Statistics
 * Saving the messages and/or other statistics into a file
 * Smart filtering dedicated to easier Prapo count

To implement another mode, simply add another case in the [prapo_data_handler.py](prapo_utils/prapo_data_handler.py) module located in the [utils](prapo_utils) folder. It is hard-coded in there. I know. But you know, it is a Python project so it is dogshit anyways :)
## Getting the source data file
To get the source data file, open WhatsApp, press the 3 dots on the top right of your screen and press More -> Export chat (->without media). You can then share the file to your PC and run the script there.
