import difflib

def is_similar_to(text, target, threshold=0.7):
    """
    	Checks if text contains a substring similar to 'prapo'
    	allowing small typos or missing letters.
    """
    text_lower = text.lower()

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
    	2.1) contain 'Prapo' in some approximate form
	    OR
	    2.2) contain <Média vynechány> since that includes Prapo-counting stickers and photos
    """
    filterCode = filterCode.lower()

    filtered = []
    for message in messages:
        msg_lower = message.lower()
        if filterCode in msg_lower and (is_similar_to(msg_lower, "prapo") or is_similar_to(msg_lower, "<Média vynechány>") or is_similar_to(msg_lower, "(file attached)")):
            filtered.append(message)

    return filtered
