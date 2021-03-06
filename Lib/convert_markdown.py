#!/usr/bin/env python
import io
import os
import sys
import json
import datetime
import xml.etree.ElementTree as ET
import markdown2


IO_PARAMS = dict(encoding='ascii', newline='\r\n')


def main(file_name):
    # print '\n\n============ converting', file_name, '============\n\n'
    tree = init_tree()
    html = tree.getroot()
    body = markdown_2_html_body(file_name)
    html.append(body)
    config = get_json(file_name)
    if config['prettyprint']:
        enable_pretty_printing(tree)
    fix_head(html, config)
    write_tree(tree, file_name)


def init_tree():
    return ET.parse('markdown/boilerplate.html')


def markdown_2_html_body(file_name):
    markdown_text = get_text('markdown/{0}.markdown'.format(file_name))
    html_text = markdown2.markdown(markdown_text)
    if file_name != 'index':
        html_text += ('\n<p>Return to <a href="index.html">' +
                      'Index Page</a></p>')
    now = datetime.datetime.now()
    html_text += ('\n<p class="footnote">Lyall Jonathan Di Trapani ' +
                  '{}</p>\n'.format(now.strftime('%d %b %Y')))
    return ET.fromstring('<body>\n{0}\n</body>'.format(html_text))


def get_text(file_name):
    with open(file_name, 'U') as markdown_file:
        return markdown_file.read()


def get_json(file_name):
    text = get_text('markdown/{0}.markdown'.format(file_name))
    title = text.split('\n', 1)[0].strip()
    config = dict(
        title=title,
        css=[],
        javascript=[],
        prettyprint=False,
    )
    json_file_name = 'markdown/{0}.json'.format(file_name)
    if os.path.exists(json_file_name):
        json_config = json.load(open(json_file_name, 'U'))
        config.update(json_config)
    return config


def enable_pretty_printing(tree):
    pre_list = tree.findall('body/pre')
    for pre in pre_list:
        code = pre.find('code')
        text = code.text
        pre.clear()
        pre.text = text
        pre.set('class', 'prettyprint linenums')
    body = tree.find('body')
    body.set('onload', 'prettyPrint()')


def fix_head(html, config):
    head = html.find('head')
    set_title(head, config['title'])
    add_css_links(head, config['css'])
    add_javascript_links(head, config['javascript'])


def set_title(head, title_text):
    title = ET.Element('title')
    title.text = title_text
    title.tail = '\n'
    head.insert(1, title)


def add_css_links(head, css_file_names):
    for css_file_name in css_file_names:
        attrib = dict(href=css_file_name,
                      rel='stylesheet',
                      type='text/css')
        element = ET.Element('link', attrib)
        element.tail = '\n'
        head.append(element)


def add_javascript_links(head, javascript_file_names):
    for javascript_file_name in javascript_file_names:
        attrib = dict(type='text/javascript', src=javascript_file_name)
        element = ET.Element('script', attrib)
        element.text = ' '        # Forces an explicit closing tag
        element.tail = '\n'
        head.append(element)


def write_tree(tree, file_name):
    html_file_name = 'website/{0}.html'.format(file_name)
    with io.open(html_file_name, 'w', **IO_PARAMS) as html_file:
        html_file.write(u'<!DOCTYPE html>\n')
        html_file.write(unicode(ET.tostring(tree.getroot())))


if __name__ == '__main__':
    file_names = (
        'index',
        'syllabus',
        'instructions',
        'zip-instructions',
        'jsbin-instructions',
        'javascript-tutorial',
        'qunit-tutorial',
        'lesson1',
        'lesson2',
        'lesson3',
        'example1',
        'example2',
        'assignment1',
        'assignment2',
        'assignment3',
    )
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if sys.argv[1] in file_names:
            main(file_name)
        else:
            template = '"{0}" not a file in file_names list\nEXIT\n'
            message = template.format(file_name)
            sys.stderr.write(message)
            sys.exit(1)
    else:
        map(main, file_names)
