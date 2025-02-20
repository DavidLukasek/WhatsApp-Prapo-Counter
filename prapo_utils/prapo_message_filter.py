def filterMessages(messages, filterCode):
    """
        Filters messages that contain the given filterCode.
    
        Args:
            messages (str[]): List of message lines.
            filterCode (str): Substring to filter messages by.
    
        Returns:
            str[]: Messages containing the filterCode.
    """
    return [message for message in messages if filterCode in message]
