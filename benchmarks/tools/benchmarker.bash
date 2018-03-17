#!/usr/bin/env bash

set -o errexit
set -o pipefail

declare -r BOLD_FONT="$(tput bold)"
declare -r RESET_FONT="$(tput sgr0)"

function get_source() {
  declare -r base_path="$1"
  declare -r base_name="$2"

  find "$base_path" \
    -maxdepth 1 \
    \( -name "${base_name}js" -o -name "${base_name}micro" \) \
    -exec cat "{}" \;
}

declare -r custom_base_path="$1"

declare -ri full_size=$(get_source "$custom_base_path" "index." | wc -m)
echo "Size of the full version: $full_size B"

declare -ri minified_size=$(get_source "$custom_base_path" "index.min." | wc -m)
echo "Size of the minified version: $BOLD_FONT$minified_size B$RESET_FONT"

declare -r saved="$(echo "scale=2; 100 - 100*$minified_size/$full_size" | bc)"
echo "Saved: $saved%"
