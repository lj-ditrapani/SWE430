# Run with ./zip-tool.sh name
css="website/css"
js="website/js"
tools="student-dev-tools"
zipfile="website"/${1}.zip
rm -f $zipfile
zip -j $zipfile ${tools}/code.js ${tools}/test.js ${css}/qunit.css \
    ${js}/qunit.js ${tools}/${1}-test.html
