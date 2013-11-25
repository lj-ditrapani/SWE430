import os
import shutil


join = os.path.join
dest = join('website', 'example1')


for file_name in ('example1-test.html', 'code.js'):
    shutil.copy2(join('student-dev-tools', file_name), dest)
for file_name in (join('css', 'qunit.css'), join('js', 'qunit.js')):
    shutil.copy2(join('website', file_name), dest)

