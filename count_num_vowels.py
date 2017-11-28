"""
Exercise 4
"""

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']


def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    whit listcomprehension
    """
    return len([i for i in s if i.lower() in VOWELS ])


def count_num_vowels_filter(s):
    """
    Returns the number of vowels in a string s.
    whit filter
    """

    return len(list(filter(lambda x: x.lower() in VOWELS, s)))
