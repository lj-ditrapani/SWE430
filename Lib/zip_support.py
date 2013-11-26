'''
Author:  Lyall Jonathan Di Trapani  ------------------------------------
Copy non git-tracked files into SWE430-support.zip
  3rd party, external libraries
  media files (.png, .pdf ...)
  Not .zip files (example.zip, SWE430.zip, ...)
Unzipping this file in the root project directory will place each file
in the correct location.
'''
import os
import zipfile


def make_support_zip_file():
    '''Create support zip file'''
    with open('.gitignore', 'U') as gitignore_file:
        text = gitignore_file.read()
    _, tail = text.split('### Begin: support files ###')
    support_files, _ = tail.split('### End: support files ###')
    zip_file = zipfile.ZipFile('SWE430-support.zip', 'w', 
                               zipfile.ZIP_DEFLATED)
    for line in support_files.split('\n'):
        handle_line(line, zip_file)
    zip_file.close()
    

def handle_line(line, zip_file):
    '''If line is a file, write to SWE340-support.zip'''
    clean_line = line.strip()
    if clean_line == '':
        return
    if clean_line[0] == '#':
        return
    file_name = clean_line[1:]
    if os.path.exists(file_name):
        zip_file.write(clean_line[1:])
    else:
        raise Exception('File {0} does not exist'.format(file_name))


if __name__ == '__main__':
    make_support_zip_file()
