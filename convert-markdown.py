import io
import os
import json
import xml.etree.ElementTree as ET
import markdown2


def main(file_name):
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
    html_text += ('\n<p class="footnote"> Lyall Jonathan Di Trapani ' +
                  '15 Nov 2013</p>\n')
    return ET.fromstring('<body>\n{0}\n</body>'.format(html_text))


def get_text(file_name):
    with io.open(file_name, encoding='ascii', newline='\r\n') as f:
        return f.read()


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
        json_config = json.load(open(json_file_name))
        config.update(json_config)
    return config


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
    f = io.open('website/{0}.html'.format(file_name),
                'w', encoding='ascii', newline='\r\n')
    f.write(u'<!DOCTYPE html>\n')
    f.write(unicode(ET.tostring(tree.getroot())))
    f.close()


if __name__ == '__main__':
    main('exercise')
