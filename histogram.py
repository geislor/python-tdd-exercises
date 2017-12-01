
def histogram(l):
    """
    Converts a list of integers into a simple string histogram.
    """

    histogram_list = ['#'*i for i in l]
    return '\n'.join(histogram_list)
