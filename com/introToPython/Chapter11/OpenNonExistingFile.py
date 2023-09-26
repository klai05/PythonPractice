try:
    infile = open('dataFile.txt', 'r')
    infile.write("hello")

    infile.close()
except IOError as ioe:
    print('filename:', ioe.filename)
    print('filename 2:', ioe.filename2)
    print('strerror:', ioe.strerror)
    print('errno:', ioe.errno)
