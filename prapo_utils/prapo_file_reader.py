def read_file_lines(file_path):
    """
        Reads all lines in the given file and returns
        them as an array of strings with striped whitespaces

        Args:
            file_path (str): File path to the Prapo chat data
        Returns:
            str[]: Array of lines with striped whitespaces
    """
    try:
        retLines = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                retLines.append(line.strip())
        return retLines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
