#Made by thoricelli 2020, ignore my terrible programming lol
import os
import re
import getpass

print("Please wait...")

path = "C:\\Users\\" + getpass.getuser() + "\\AppData\\Local\\Temp\\Roblox"
path2 = os.getcwd()
ExportPath = path2 + "\\Export\\"
os.chdir(path)

if not os.path.isdir(ExportPath):
	os.mkdir(ExportPath)

arr = os.listdir("http/")
for i in arr:
	if not os.path.isfile(ExportPath + i):
		f = open("http/" + i,"r")
		lines = 0
		curlines = 0
		for lines in f:
			curlines = curlines+1
			if lines.find("PNG",1,4) == 1:
				print("Found image")
				c = open(ExportPath + i + '.png', "wb+")
				count = 0
				f.close()
				f = open("http/" + i,"rb")
				for x in f:
					count = count + 1
					if count > curlines-1:
						c.write(x)
				c.close()
				break
			if lines == "Content-Type: audio/mpeg\n": #For some reason find wouldn't work...
				print("Found audio")
				c = open(ExportPath + i + '.mp3', "wb+")
				count = 0
				f.close()
				f = open("http/" + i,"rb")
				for x in f:
					count = count + 1
					if count > curlines+12:
						c.write(x)
				c.close()
				break
		f.close()
print("Done!")
raw_input("Press Enter to continue...")
