import sys
import markdown2


def get_text(file_name):
    f = open(file_name)
    text = f.read()
    f.close()
    return text


def convert(file_name):
    text = get_text(file_name)
    return markdown2.markdown(text)

file_name = 'exercise'
html = convert('markdown/{0}.markdown'.format(file_name))
#head = get_text('html-fragments/head.html')
head = get_text('markdown/head.html')

f = open('website/{0}.html'.format(file_name), 'w')
f.write(head)
f.write(html)
f.write('\n</body></html>\n')
f.close()
