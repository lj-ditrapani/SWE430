# Copy non git-tracked files into SWE430-support.zip
#   3rd party, external libraries
#   media files (.png, .pdf ...)
#   Not .zip files (example.zip, SWE430-website.zip, ...)
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
    print line,
    if line[0] == '#':
        print 'comment'
        continue
    clean_line = line.strip()
    if clean_line == '':
        continue
        print 'empty'
    print 'file'
    zip_file.write(clean_line[1:])
zip_file.close()



zip_name = 'SWE430.zip'
if os.path.exists(zip_name):
    os.remove(zip_name)
zip_folder('website', zip_name)
