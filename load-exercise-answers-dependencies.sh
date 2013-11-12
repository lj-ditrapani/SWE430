# copy dependencies of exercise answers from student-dev-tools &
# website into exercise-answers and exercise-first-steps
# (exercise-tests.html, qunit.js, qunit.css)
dir1=exam-and-exercise-answers/exercise-answers
dir2=exam-and-exercise-answers/exercise-first-steps
tools=student-dev-tools
cp ${tools}/exercise-test.html $dir1
cp ${tools}/exercise-test.html $dir2
cp website/js/qunit.js $dir1
cp website/js/qunit.js $dir2
cp website/css/qunit.css $dir1
cp website/css/qunit.css $dir2
