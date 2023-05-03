#!/bin/bash

function get_boundary {
    title="$1"
    line_len="${2:-79}"
    title_len="${#title}"
    is_even=$(( (line_len + title_len) % 2 ))

    if [[ "$is_even" -eq 0 ]]; then
        left_dash=$(get_dash_length "$line_len" "$title_len")
        right_dash="$left_dash"
    else
        left_dash=$(get_dash_length "$line_len" "$title_len")
        right_dash=$((left_dash + 1))
    fi

    if [[ $((line_len - 6)) -gt "$title_len" ]]; then
        printf "# %s %s %s #\n" "$(repeat_char "-" "$left_dash")" "$title" "$(repeat_char "-" "$right_dash")"
    else
        echo "The title name is too long!"
    fi
}

function get_dash_length {
    line_len="$1"
    title_len="$2"
    echo $(( (line_len - 6 - title_len) / 2 ))
}

function repeat_char {
    char="$1"
    count="$2"
    printf "%-${count}s" "$char" | tr ' ' "$char"
}

if [[ $# -lt 1 ]]; then
    echo "Please supply a title for the separator"
    exit 1
fi

title="$1"
line_len="${2:-79}"

get_boundary "$title" "$line_len"

