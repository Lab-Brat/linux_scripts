#!/usr/bin/python3
import sys

# ------------------------------ Script Logic ------------------------------- #
def get_boundary(title, line_len):
    '''
    Print a line separator of length 79 (PEP8 recommendation) 
    with a title in the middle
    '''
    if line_len is None:
        line_len = 79
    title_len = len(title)
    is_even = (line_len + title_len) % 2 == 0

    if is_even:
        left_dash = right_dash = get_dash_length(line_len, title_len)
    else:
        left_dash = right_dash = get_dash_length(line_len, title_len)
        right_dash += 1

    if line_len-6 > len(title):
        print(f"# {'-'*left_dash} {title} {'-'*right_dash} #")
    else:
        print('The title name is too long!')


def get_dash_length(line_len, title_len):
    '''
    Helper function
    Return the amount of dashes needed in a separator
    6 is the length of 2 # symbols and 4 extra spaces
    '''
    return (line_len - 6 - title_len) // 2


# ------------------------------- Run Script -------------------------------- #
if __name__ == '__main__':
    try:
        title = sys.argv[1]
    except IndexError:
        print('Please supply a title for the separator')
        sys.exit(1)

    get_boundary(title)


# Run in the console:
# >---> python create_boundary.py "Testing Script's Functionality"
#
# Result:
# --------------------- Testing Script's Functionality ---------------------- #
