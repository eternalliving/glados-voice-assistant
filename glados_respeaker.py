#!/usr/bin/python3
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.dirname(os.path.abspath(__file__))+'/settings.env')

if(os.getenv('RESPEAKER_CONNECTED')):
	try:
		from pixel_ring import pixel_ring
	except Exception as e:		
		print("run sudo pip3 install pixel_ring")

def respeaker_pixel_ring(rgb=0x200000):

	# Set respeaker to dim glow inside the head.
	# See hardware folder for more info.
	try:
		pixel_ring.set_color(rgb)
	except Exception as e:
		print(e)


def respeaker_mode(mode):

	if(mode == "listen"):
		try:
			pixel_ring.listen()
		except Exception as e:
			print(e)
	elif(mode == "wait"):
		try:
			pixel_ring.wait() 
		except Exception as e:
			print(e)