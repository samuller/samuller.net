#!/bin/bash
#
# Script for running commonly used commands quickly, e.g. "./run.sh html". See: "./run.sh help".
#

# Fail on first error.
set -e

# Make uv commands faster, but requires dependencies to have already been fetched & cached
UV_OFFLINE=true

OUTPUTDIR=output

man_help="List all commands available."
help() {
    echo "You have to provide a command to run, e.g. '$0 html'"
    # List declared functions that are not from exports (-fx).
    commands=$(echo "$KNOWN_COMMANDS" | cut -d' ' -f 3 | tr '\n' ' ')
    echo "All commands available are:"
    echo
    (
        for cmd in ${commands}; do
            doc_name=man_$(echo "$cmd" | tr - _)
            # TODO: use fold for long descriptions?
            printf "  %-15s %-57s\n" "$cmd" "${!doc_name}"
        done
    ) | column -t -s$'\t'
    echo
    exit
}

man_css="Compile SASS to theme/static/css/main.css."
css() {
    uv run python -c "
import sass, os
with open('css/main.scss') as f:
    content = f.read()
if content.startswith('---'):
    content = content.split('---', 2)[2]
os.makedirs('theme/static/css', exist_ok=True)
css = sass.compile(string=content, include_paths=[os.path.abspath('_sass'), os.path.abspath('css')])
open('theme/static/css/main.css', 'w').write(css)
"
}

man_html="Build the site with the dev config."
html() {
    css
    uv run pelican content -o "$OUTPUTDIR" -s pelicanconf.py
}

man_publish="Build the site with the production config."
publish() {
    css
    uv run pelican content -o "$OUTPUTDIR" -s publishconf.py
}

man_clean="Remove the output directory."
clean() {
    rm -rf "$OUTPUTDIR"
}

man_serve="Build (dev) then serve the output on http://localhost:4000."
serve() {
    html
    uv run python -m http.server 4000 --directory "$OUTPUTDIR"
}

# Find all declared functions that are not from exports (-fx). This will only pick up functions before this point.
KNOWN_COMMANDS=$(declare -F | grep -v "\-fx")

# If column command is not available, create a no-op function to replace it and prevent errors.
# Alternatively, install it with: apt-get install -y bsdmainutils
if ! type column >/dev/null 2>&1
then function column { cat - ;}
fi

# Run function with same name of CLI argument (default to "help").
cmd=${1:-"help"}
if [ "$#" -gt 0 ]; then
    # Remove argument we've already used.
    shift
fi
$cmd "$@"
