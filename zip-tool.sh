# Run with sh zip-tool.sh name code-file test-file base-tail
css="website/css"
js="website/js"
base="website/430"$4
tools="student-dev-tools"
rm -f ${base}/${1}.zip
zip -j ${base}/${1}.zip ${2}.coffee ${js}/coffee-script.js ${css}/qunit.css ${js}/qunit.js ${3}.coffee ${tools}/${1}-test.html
