#sense hat test 1.1
from sense_emu import SenseHat
from random import randint
sense = SenseHat()

r=randint(0,255)
g=randint(0,255)
b=randint(0,255)

sense.set_pixel(0,0,r,g,b)

#display color


# define scoll speed
sense.scroll_speed = 15

#send message
sense.show_message("this is colourful", text_colour=(r,g,b)) 
print r,g,b
