#!/bin/bash

zone="${1:-public}"
sources=$(sudo firewall-cmd --zone "${zone}" --list-sources | tr " " "\n" | sort -h)

echo "Networks:"
for source in "${sources}"; do
    if echo "${source}" | grep -q '/' && ! echo "${source}" | grep -q '/32'; then
        echo "- $source"
    fi
done

echo -e "\nIP addresses:"
for source in "${sources}"; do
    if echo "${source}" | grep -q '/32' || ! echo "${source}" | grep -q '/'; then
        echo "- \"${source%/*}\""
    fi
done

