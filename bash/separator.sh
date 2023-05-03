#!/bin/bash

# Print a line separator with a title in the middle
# Arguments:
#   $1: title - The title to be displayed in the middle of 
#       the line separator
#   $2: line_len - The total length of the line separator, 
#       including the title (optional, default: 79)
function get_boundary {
    title="$1"
    line_len="${2:-79}"
    title_len="${#title}"
    is_even=$(( (line_len + title_len) % 2 ))

    if [[ "$is_even" -eq 0 ]]
    then
        left_dash=$(get_dash_length "$line_len" "$title_len")
        right_dash="$left_dash"
    else
        left_dash=$(get_dash_length "$line_len" "$title_len")
        right_dash=$((left_dash + 1))
    fi

    if [[ $((line_len - 6)) -gt "$title_len" ]]
    then
        printf "# %s %s %s #\n" \
               "$(repeat_char "-" "$left_dash")" \
               "$title" \
               "$(repeat_char "-" "$right_dash")"
    else
        echo "The title name is too long!"
    fi
}

# Calculate the number of dashes needed in a line separator
# on each side of the title
# Arguments:
#   $1: line_len - The total length of the line separator, 
#       including the title
#   $2: title_len - The length of the title
# Output:
#   Returns the number of dashes needed on each side of the title
function get_dash_length {
    line_len="$1"
    title_len="$2"
    echo $(( (line_len - 6 - title_len) / 2 ))
}

# Repeat a character a specified number of times
# Arguments:
#   $1: char - The character to be repeated
#   $2: count - The number of times to repeat the character
# Output:
#   Returns a string with the character repeated the 
#   specified number of times
function repeat_char {
    char="$1"
    count="$2"
    printf "%-${count}s" "$char" | tr ' ' "$char"
}

# Raise exception if number of command parameters are < 1
if [[ $# -lt 1 ]]; then
    echo "Please supply a title for the separator"
    exit 1
fi

title="$1"
line_len="${2:-79}"

get_boundary "$title" "$line_len"

