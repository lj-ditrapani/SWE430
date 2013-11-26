# Author:  Lyall Jonathan Di Trapani  ==================================
import os
import shutil


join = os.path.join
SDT = 'student-dev-tools'
WEB = 'website'
EAA = 'exam-and-assignment-answers'


def create_dev_environment(name):
    if name == 'assignment1':
        dest = 'assignment1-dev'
        shutil.copy2(join(EAA, 'assignment1', 'code.js'), dest)
    elif name in ('assignment2', 'assignment3'):
        dest = join(EAA, name)
    else:      # example1 or example2
        dest = join(WEB, name)
    shutil.copy2(join(SDT, name + '-test.html'), dest)
    for file_name in (join('css', 'qunit.css'), join('js', 'qunit.js')):
        shutil.copy2(join(WEB, file_name), dest)


names = ('example1', 'example2',
         'assignment1', 'assignment2', 'assignment3')
for name in names:
    create_dev_environment(name)
