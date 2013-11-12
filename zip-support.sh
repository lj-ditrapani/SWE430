# Copy non git-tracked files into SWE430-support.zip
#   3rd party, external libraries
#   media files (.png, .pdf ...)
#   Not .zip files (example.zip, SWE430-website.zip, ...)
# Unzipping this file in the root project directory will place each file
# in the correct location.
name="SWE430-support.zip"
rm -f $name
zip $name website/css/prettify.css website/css/qunit.css \
website/js/coffee-script.js website/js/prettify.js website/js/qunit.js \
website/js/ljd-utils.js \
website/lesson1/cycles.png wbesite/lesson1/legacy.png \
support/language_comparison_prechelt.pdf

