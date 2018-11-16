import subprocess
import os

imageExtensions = {'.jpg','.png','.jpeg','.bmp'}

directory = input('Insert the directory of images :')
print ("""


	
.............................................................
.............................................................
.............................................................
.............................................................
.............................................................
Converting images into webp in : """ + directory)

print ("Current: " + os.getcwd())
os.chdir(directory)
print ("Changed to: " + os.getcwd())

files = os.listdir(directory)
print("files:\n" + ' '.join(files))

for fil in files:

	extension = fil[fil.rfind('.'):]

	if  extension in imageExtensions:
		
		newName = fil.replace(extension,".webp")

		terminalCmd = 'cwebp -q 20 "{}" -o "{}"'.format(fil,newName)
		# terminalCmd = 'mv "{}" "{}"'.format(fil,newName) # Just for testing, I don't have cwebp.

		subprocess.call(terminalCmd,shell=True)
		subprocess.call('ls')
