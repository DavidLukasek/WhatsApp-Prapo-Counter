import difflib

def is_similar_to_prapo(text, threshold=0.7):
    """
    Checks if text contains a substring similar to 'prapo'
    allowing small typos or missing letters.
    """
    text_lower = text.lower()
    target = "prapo"

    for i in range(len(text_lower) - len(target) + 1):
        substring = text_lower[i:i + len(target)]
        similarity = difflib.SequenceMatcher(None, substring, target).ratio()
        if similarity >= threshold:
            return True

    return False


def filterMessages(messages, filterCode):
    """
    Filters messages that:
    1) contain the user-provided filterCode
    AND
    2) contain 'Prapo' in some approximate form
    """
    filterCode = filterCode.lower()

    filtered = []
    for message in messages:
        msg_lower = message.lower()
        if filterCode in msg_lower and is_similar_to_prapo(msg_lower):
            filtered.append(message)

    return filtered
