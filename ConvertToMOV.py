import sys
import re
import subprocess

print("Convert to MOV by Kemote")

tmp = ""
file = sys.argv[1].split("\\")[-1]
path = sys.argv[1].split("\\")[0:-1]
format = sys.argv[1].split(".")[-1]
for i in path:
	tmp +=(i + "\\")
path = tmp
index = re.findall("\d+", file)[-1]
index = "%0" + str(len(index)) + "d"
file = file[0:-(len(index) + len(format) +1)]

print(index)
print(format)	
print(file)
print(path)

subprocess.call(['ffmpeg', '-i', file + index +  "." + format, 'output.mov'])