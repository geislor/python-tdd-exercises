

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    
    return max(s.split(' '), key=len)

