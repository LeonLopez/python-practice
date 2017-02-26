import os

def rename_files():
	#get the files name in the folder
	filenames = os.listdir(r"E:\python_resources\alphabet")
	print filenames
	os.chdir(r"E:\python_resources\alphabet")

	#for each file name,rename it
	for filename in filenames:
		print('old file name is',filename)
		print('new file name is',filename.translate(None,"abcdefg"))
		os.rename(filename,filename.translate(None,"abcdefg"))
rename_files()