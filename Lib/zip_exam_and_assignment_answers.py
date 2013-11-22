#! /usr/bin/env python
import os
import distutils.archive_util


folder_name = 'exam-and-assignment-answers'
zip_name = 'SWE430-' + folder_name
zip_file = zip_name + '.zip'
if os.path.exists(zip_file):
    os.remove(zip_file)
distutils.archive_util.make_zipfile(zip_name, folder_name)
