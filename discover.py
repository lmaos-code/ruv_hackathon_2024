from nanoleafapi import Nanoleaf 
import github 
import time
from random import randint

nl = Nanoleaf("192.168.2.1")

g = github.Github()

repo = g.get_repo("lmaos-code/ruv_hackathon_2024")

while 1:
	print("evaluating content")
	#check file contents
	contents = repo.get_contents("test.txt", ref="main").decoded_content.decode("utf-8")
	print(contents)
	if "incident" in contents:
		nl.set_color((255, 0, 0))
	elif "change" in contents:
		nl.set_color((0, 255, 0))
	time.sleep(10) # every 10 seconds

