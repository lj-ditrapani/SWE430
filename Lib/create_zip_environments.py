# Author:  Lyall Jonathan Di Trapani ===================================
import os
import zipfile


join = os.path.join
SDT = 'student-dev-tools'
WEB = 'website'


def create_zip_environment(name):
    if name == 'example1':
        # Example 1 uses a predifned test.js file
        test_js = join(WEB, name, 'test.js')
    elif name == 'assignment1':
        # Assignment 1 uses a predifned test.js file
        test_js = join('assignment1-dev', 'test.js')
    else:
        # All others use blank test file
        test_js = join(SDT, 'test.js')
    zip_name = join(WEB, name + '.zip')
    zip_file = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    test_html = name + '-test.html'
    name_pairs = (
        (join(SDT, test_html), test_html),
        (join(WEB, 'js', 'qunit.js'), 'qunit.js'),
        (join(WEB, 'css', 'qunit.css'), 'qunit.css'),
        (join(SDT, 'code.js'), 'code.js'),
        (test_js, 'test.js')
    )
    for path, name in name_pairs:
        zip_file.write(path, name)
    zip_file.close()


if __name__ == '__main__':
    names = ('example1', 'example2',
             'assignment1', 'assignment2', 'assignment3')
    for name in names:
        create_zip_environment(name)
