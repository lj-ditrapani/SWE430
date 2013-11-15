import zipfile

zip = zipfile.ZipFile('python.zip', 'r')
file('one.txt', 'w').write(zip.read('testmd.py'))
file('two.txt', 'wb').write(zip.read('test.markdown'))
zip.close()
