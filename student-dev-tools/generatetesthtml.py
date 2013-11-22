#! /usr/bin/env python


def make_html_file(name):
    with open('template-test.html', 'rb') as template_file:
        html_template = template_file.read()
    title = '{0} {1}'.format(name[0:-1].title(), name[-1])
    html = html_template.format(title=title)
    file_name = name + '-test.html'
    with open(file_name, 'wb') as html_file:
        html_file.write(unicode(html))


if __name__ == '__main__':
    names = (
        'example1',
        'example2',
        'assignment1',
        'assignment2',
        'assignment3',
    )
    for name in names:
        make_html_file(name)
