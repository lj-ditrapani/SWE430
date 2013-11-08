tools="student-dev-tools"
code=${tools}/code
test=${tools}/test
sh zip-tool.sh example1 ${code} ${test} /example1
sh zip-tool.sh exercise1 ${code} ${test}
path="website/430/example2"
code=${path}/original
test=${path}/test-original
sh zip-tool.sh example2 ${code} ${test} /example2
path="exercise_answers/exercise2"
code=${path}/code
test=${path}/test
sh zip-tool.sh exercise2 ${code} ${test}
