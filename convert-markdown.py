import sys
import json
import xml.etree.ElementTree as ET
import markdown2


def main(file_name):
    tree = init_tree()
    html = tree.getroot()
    body = markdown2html(file_name)
    html.append(body)
    config = get_json(file_name)
    if config['prettyprint']:
        enable_pretty_printing(tree)
    fix_head(html, config)
    write_tree(tree, file_name)


def get_text(file_name):
    f = open(file_name)
    text = f.read()
    f.close()
    return text


def init_tree():
    tree = ET.ElementTree()
    tree.parse('markdown/boilerplate.html')
    return tree


def markdown2html(file_name):
    markdown_text = get_text('markdown/{0}.markdown'.format(file_name))
    html_text = markdown2.markdown(markdown_text)
    body = ET.fromstring('<body>\n{0}\n</body>'.format(html_text))
    return body


def get_json(file_name):
    return json.load(open('markdown/{0}.json'.format(file_name)))


def enable_pretty_printing(tree):
    pre_list = tree.findall('body/pre')
    for pre in pre_list:
        pre.set('class', 'prettyprint')
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
        e = ET.Element('link', attrib)
        e.tail = '\n'
        head.append(e)


def add_javascript_links(head, javascript_file_names):
    for javascript_file_name in javascript_file_names:
        attrib = dict(type='text/javascript', src=javascript_file_name)
        e = ET.Element('script', attrib)
        e.text = ' '        # Forces an explicit closing tag
        e.tail = '\n'
        head.append(e)


def write_tree(tree, file_name):
    f = open('website/{0}.html'.format(file_name), 'w')
    f.write('<!DOCTYPE html>\n')
    tree.write(f)
    f.close()


if __name__ == '__main__':
    main('exercise')
