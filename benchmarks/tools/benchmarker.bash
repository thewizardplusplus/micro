#!/usr/bin/env bash

set -o errexit
set -o pipefail

declare -r BOLD_FONT="$(tput bold)"
declare -r RESET_FONT="$(tput sgr0)"

function get_language() {
  declare -r _filename="$(basename "$(pwd)")"
  declare -r _extension="${_filename##*.}"
  echo "$_extension"
}

function get_source() {
  declare -r _script_path="$1"
  declare -r _language="$2"
  declare -r _extension="$3"

  cat "$_script_path/../virtual-dom.$_language/index$_extension.$_language"
}

declare -r language="${1:-$(get_language)}"

declare -r script_path="$(dirname "$0")"
declare -ri full_size=$(get_source "$script_path" "$language" | wc -m)
echo "Size of the full version: $full_size B"

declare -ri minified_size=$(get_source "$script_path" "$language" .min | wc -m)
echo "Size of the minified version: $BOLD_FONT$minified_size B$RESET_FONT"

declare -r saved="$(echo "scale=2; 100 - 100*$minified_size/$full_size" | bc)"
echo "Saved: $saved%"
