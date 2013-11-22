#! /usr/bin/env python
import os
import zipfile


def zip_folder(folder_name, zip_name):
    rootlen = len(folder_name) + 1
    zip_file = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for base, folders, files in os.walk(folder_name):
        for file in files:
            file_name = os.path.join(base, file)
            zip_file.write(file_name, file_name[rootlen:])


zip_name = 'SWE430.zip'
if os.path.exists(zip_name):
    os.remove(zip_name)
zip_folder('website', zip_name)
