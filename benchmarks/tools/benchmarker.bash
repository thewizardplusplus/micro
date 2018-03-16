#!/usr/bin/env bash

declare -r BOLD_FONT="$(tput bold)"
declare -r RESET_FONT="$(tput sgr0)"

declare -r base_path="$1"

declare -ri full_size=$(cat "$base_path/index.js" | wc -m)
echo "Size of the full version: $full_size B"

declare -ri minified_size=$(cat "$base_path/index.min.js" | wc -m)
echo "Size of the minified version: $BOLD_FONT$minified_size B$RESET_FONT"

declare -r saved="$(echo "scale=2; 100 - 100*$minified_size/$full_size" | bc)"
echo "Saved: $saved%"
