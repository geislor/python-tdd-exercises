
def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    s_list = [len(i) for i in s.split(' ')]
    return s_list