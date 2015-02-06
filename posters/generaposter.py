import sys
import subprocess

title = sys.argv[1]
name = sys.argv[2]
date = sys.argv[3]
address  = sys.argv[4]
print(sys.argv)

f = open('BFSposter.svg')
filecontents = f.read()

filecontents=filecontents.replace('TITLE', title)
filecontents=filecontents.replace('NAME', name)
filecontents=filecontents.replace('TALKDATE', date)
filecontents=filecontents.replace('ADDRESS', address)

outputpath = 'generated-poster.svg'
towrite=open(outputpath, 'w')
towrite.write(filecontents)
towrite.close()

subprocess.call(["inkscape", outputpath, "--export-pdf=poster.pdf"])

