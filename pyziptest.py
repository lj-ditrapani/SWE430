import zipfile

zip = zipfile.ZipFile('python.zip', 'w')
zip.write('testmd.py')
zip.write('test.markdown')
zip.close()
