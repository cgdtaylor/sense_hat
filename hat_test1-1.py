#sense hat test 1.1
from sense_emu import SenseHat
from random import randint
from time import sleep 
sense = SenseHat()
#display color
i=0

j=0

while 1==1:
	while j<=7:
		while i <=7:
		
			r=randint(0,255)
			g=randint(0,255)
			b=randint(0,255)
			
			sense.set_pixel(i,j,r,g,b)
			i=i+1
		
			
			#if p>=8:
				#break
			sleep(0.05)
		i=0
	
		j=j+1
		
	j=0
	
# define scoll speed
#sense.scroll_speed = 15

#send message
#sense.show_message("this is colourful", text_colour=(r,g,b)) 
print(p,j) 
