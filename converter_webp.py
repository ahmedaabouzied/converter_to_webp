import subprocess
import os
directory = input('Insert the directory of images :')
print ("""


	
	.............................................................
	.............................................................
	.............................................................
	.............................................................
	.............................................................
	Converting images 'png , jpg ' into webp in :""" + directory)
files = os.listdir( directory)
print (os.getcwd())
os.chdir( directory)
print (os.getcwd())
for file in files:
	originalName = file.replace(" ","") .lower()
	os.rename(file,originalName) 
	formattedName = file .replace(".png", "") .replace(".jpg", "")
	newName = file.replace(".png",".webp") .replace(".jpg",".webp")
	terminalCmd = "cwebp -q 20 "+originalName+" -o "+newName
	subprocess.call(terminalCmd , shell=True)
	subprocess.call(['ls'])