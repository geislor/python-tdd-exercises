"""
Exercise 3
"""

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

def is_english_vowel(character):
    """
    Returns True if character is an english vowel
    and False otherwise.
    """
    return character.lower() in VOWELS
