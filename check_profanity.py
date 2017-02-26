import urllib

def read_text():
	file = open('E:\python_demo\movie_quotes.txt')
	text = file.read()
	print(text)
	file.close()
	check_profanity(text)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
	output = connection.read()
	print(output)
	connection.close()

read_text()