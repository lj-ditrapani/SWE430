import sys
import json
import xml.etree.ElementTree as ET
import markdown2


def get_text(file_name):
    f = open(file_name)
    text = f.read()
    f.close()
    return text


def convert(file_name):
    markdown_text = get_text('markdown/{0}.markdown'.format(file_name))
    html_text = markdown2.markdown(markdown_text)
    body = ET.fromstring('<body>\n{0}\n</body>'.format(html_text))
    return body


def init_tree():
    tree = ET.ElementTree()
    tree.parse('markdown/boilerplate.html')
    return tree


def get_json(file_name):
    return json.load(open('markdown/{0}.json'.format(file_name)))


file_name = 'exercise'
body = convert(file_name)
tree = init_tree()
html = tree.getroot()
html.append(body)
pre_list = tree.findall('body/pre')
for pre in pre_list:
    pre.set('class', 'prettyprint')
config = get_json(file_name)
if config['prettyprint']:
    body.set('onload', 'prettyPrint()')
head = html.find('head')
title = ET.Element('title')
title.text = config['title']
title.tail = '\n'
head.insert(1, title)
for css_file_name in config['css']:
    attrib = dict(rel='stylesheet', href=css_file_name, type='text/css')
    e = ET.Element('link', attrib)
    e.tail = '\n'
    head.append(e)
for js_file_name in config['js']:
    attrib = dict(type='text/javascript', src=js_file_name)
    e = ET.Element('script', attrib)
    e.text = ' '
    e.tail = '\n'
    head.append(e)
f = open('website/{0}.html'.format(file_name), 'w')
tree.write(f)
f.close()
