import os
import zipfile


join = os.path.join
SDT = 'student-dev-tools'
WS = 'website'


def create_zip_environment(name):
    if name in ('example1', 'assignment1'):
        test_js = join('website', name, 'test.js')
    else:
        test_js = join(SDT, 'test.js')
    zip_name = join('website', name + '.zip')
    zip_file = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    test_html = name + '-test.html'
    name_pairs = (
        (join(SDT, test_html), test_html),
        (join(WS, 'js', 'qunit.js'), 'qunit.js'),
        (join(WS, 'css', 'qunit.css'), 'qunit.css'),
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
