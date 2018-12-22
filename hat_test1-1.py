#sense hat test 1.1
from sense_emu import SenseHat
from random import randint
from time import sleep 
sense = SenseHat()
#display color
i=0
while i <=10:

	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	
	sense.set_pixel(0,0,r,g,b)
	i=i+1
	sleep(2)



# define scoll speed
#sense.scroll_speed = 15

#send message
#sense.show_message("this is colourful", text_colour=(r,g,b)) 
print i 
