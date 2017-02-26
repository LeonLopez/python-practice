import time
import webbrowser

total_break = 3
break_count = 0
while(break_count < total_break):
	
	time.sleep(10)
	webbrowser.open("http://play.baidu.com/?__m=mboxCtrl.playSong&__a=8884770&__o=song/8884770||playBtn&fr=-1||play.baidu.com#")
	break_count+=1