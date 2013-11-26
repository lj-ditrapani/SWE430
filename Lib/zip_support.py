# Copy non git-tracked files into SWE430-support.zip
#   3rd party, external libraries
#   media files (.png, .pdf ...)
#   Not .zip files (example.zip, SWE430.zip, ...)
# Unzipping this file in the root project directory will place each file
# in the correct location.
import os
import zipfile


zip_file_name = 'SWE430-support.zip'


with open('.gitignore', 'U') as gitignore_file:
    text = gitignore_file.read()
_, tail = text.split('### Begin: support files ###')
support_files, _ = tail.split('### End: support files ###')
zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
for line in support_files.split('\n'):
    clean_line = line.strip()
    if clean_line == '':
        print '  empty:', line[:14]
        continue
    if clean_line[0] == '#':
        print 'comment:', line[:14]
        continue
    print '   file:', line[:14]
    file_name = clean_line[1:]
    if os.path.exists(file_name):
        zip_file.write(clean_line[1:])
    else:
        raise Exception('File {0} does not exist'.format(file_name))
zip_file.close()
