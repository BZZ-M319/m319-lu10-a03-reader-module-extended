"""
input_reader module with input validation
"""


def read_float(text_to_display, lower_bound=None, upper_bound=None):
    """
    Read a float from the user within bounds
    @param text_to_display: the text to display to the user
    @param lower_bound: the lower bound of the input
    @param upper_bound: the upper bound of the input
    @return: the float entered by the user
    """
    while True:
        try:
            num = float(input(text_to_display))
        except ValueError:
            print("Please, enter a real number!")
            continue
        else:
            if lower_bound is not None and num < lower_bound:
                print("Please, enter a number greater than or equal to", lower_bound)
                continue
            if upper_bound is not None and num > upper_bound:
                print("Please, enter a number less than or equal to", upper_bound)
                continue
            return num


def read_int(text_to_display, lower_bound=None, upper_bound=None):
    """
    Read an int from the user within bounds
    @param text_to_display: the text to display to the user
    @param lower_bound: the lower bound of the input
    @param upper_bound: the upper bound of the input
    @return: the int entered by the user
    """
    while True:
        try:
            num = int(input(text_to_display))
        except ValueError:
            print("Please, enter a whole number!")
            continue
        else:
            if lower_bound is not None and num < lower_bound:
                print("Please, enter a number greater than or equal to", lower_bound)
                continue
            if upper_bound is not None and num > upper_bound:
                print("Please, enter a number less than or equal to", upper_bound)
                continue
            return num