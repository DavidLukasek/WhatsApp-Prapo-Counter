def handle_data(filteredMessages, mode):
    """
        Handles the data based on the given mode value.

        Currently implemented modes are:

        1 - Prints the number of filtered messages

        2 - Prints the filtered messages

        3 - Saves the filtered messages into a .txt file

        Args:
            filteredMessages (str[]): List of message lines to work with
            mode (int): flag representing what to do with the data
    """
    match mode:
        case 1:
            print(f"Number of filtered messages: {len(filteredMessages)}")
        case 2:
            print("Filtered messages:")
            for message in filteredMessages:
                print(message)
        case _:
            print("Error: Invalid mode value!\nPossible mode values: 1 2.")
