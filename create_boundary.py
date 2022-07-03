import sys

# ------------------------------ Script Logic ------------------------------- #
def get_boundary(line_len, title):
    '''
    Print a line separator of length 79 (PEP8 recommendation) 
    with a title in the middle
    '''
    title_len = len(title)

    if (line_len + title_len) % 2 == 0:
        left_dash = right_dash = get_dash_length(line_len, title_len)
    elif (line_len + title_len) % 2 != 0:
        left_dash = get_dash_length(line_len, title_len)
        right_dash = get_dash_length(line_len, title_len) + 1

    print(f"# {'-'*left_dash} {title} {'-'*right_dash} #")

def get_dash_length(line_len, title_len):
    '''
    Helper function
    Return the amount of dashes needed in a separator
    6 is the length of 2 # symbols and 4 extra spaces
    '''
    return (line_len - 6 - title_len) // 2


# ------------------------------- Run Script -------------------------------- #
if __name__ == '__main__':
    TITLE = sys.argv[1]
    LINE_LEN = 79

    err = 'The title name is too long!'
    get_boundary(LINE_LEN, TITLE) if LINE_LEN > len(TITLE) else print(err)


# Run in the console:
# >---> python create_boundary.py "Testing Script's Functionality"
#
# Result:
# --------------------- Testing Script's Functionality ---------------------- #
