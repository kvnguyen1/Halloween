import board
import time
import neopixel
import random


num_pixels = 10
BRIGHTNESS = 0.1
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=1.0, auto_write=False)


'''
Function: fire
Description: Creates a lightning effect
Parameters: background: base color for lightning, foreground: color used to flash/flicker
return value: none
'''
def fire(background, foreground):
    for j in range(45):
        intensity = random.random() * 0.7 + 0.3
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        for i in range(random.randint(2, int(num_pixels/5))):
            intensity = random.random() * 0.7 + 0.3
            i_foreground = [int(i * intensity) for i in foreground]
            np[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(0.06)

'''
Function: light
Description: Creates lightning
Parameters: back: base color for lightning, fore: color used to flash
return value: none
'''
def light(back, fore):
    ran = random.random()/20
    for j in range(10):
        intense = random.random() * 0.7 + 0.3
        i_back = [int(i * intense) for i in back]
        np.fill(i_back)
        for i in range(random.randint(2, int(num_pixels/5))):
            intense = random.random() * 0.7 + 0.3
            i_fore = [int(i * intense) for i in fore]
            np[random.randint(0, num_pixels-1)] = i_fore
        np.show()
        time.sleep(ran)

'''
Function: fade_in
Description: neopixels start at the color black and then slowly fades into a color through the parameter color
Parameters: color -  the color that fades in, increment - the time of the changes
Return value: none
'''
def fade_in(color, increment):
    rgb = color
    r, g, b = rgb
    r_final = r
    g_final = g
    b_final = b
    print(r_final, g_final, b_final)
    maximum = max(rgb[0], max(rgb[1], rgb[2]))
    r_inc = rgb[0] / maximum
    g_inc = rgb[1] / maximum
    b_inc = rgb[2] / maximum
    r, g, b = 0, 0, 0
    while r <= r_final and g <= g_final and b <= b_final:
        r += r_inc
        g += g_inc
        b += b_inc
        np.fill((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)

'''
function: fade_out
description: slowly changes the color passed through to black
parameters - rgb: color that is fading, delay: the time between the changes
return value: none
'''
def fade_out(color, increment):
    rgb = color
    maximum = max (rgb[0], max(rgb[1], rgb[2]))
    r_inc = rgb[0] / maximum
    g_inc = rgb[1] / maximum
    b_inc = rgb[2] / maximum
    r, g, b = rgb
    while r >= 0 and g >= 0 and b >= 0:
        r -= r_inc
        g -= g_inc
        b -= b_inc
        np.fill((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)

'''
function: chase
description: involves two colors, one base and the other is placed in every nth neopixel.
The colors are shifted one neopixel to form a rotating pattern. 
parameters - color1: background, color2: color placed in every nth neopixel, loop: number of 
rotations, count: shifting number, delay: the time between the changes
return value: none
'''
def chase(color1, color2, loop=15, count=3, delay=0.1):
    result = 0
    for outer in range(count*loop):
        np.fill(color1)
        for i in range(num_pixels):
            if i % count == result:
                np[i] = color2
        np.show()
        time.sleep(delay)
        result += 1
        result %= count

'''
Function: sparkle
Description: has a background color (through color parameter) and it chooses a random number of neopixels to flash white, imitating a sparkle effect
Parameters - color: the background color, delay: the time between the changes, loop: the number of sparkles
Return value: none
'''
def sparkle(color1, color2, loop = 30, delay=0.1):
  for outer in range(loop):
    np.fill(color1)
    for i in range(np.n / 4):
      np[random.randint(0, np.n-1)] = color2
    np.show()
    time.sleep(delay)
    
while True:
    for i in range(3):
        fire((36, 2, 120), (95, 52, 145))
        light((255, 129, 0), (255, 129, 0))
    fire((36, 2, 120), (95, 52, 145))
    fade_out([36, 2, 120], 0.01)
    fade_in([0, 75, 0], 0.01)
    fade_out([0, 75, 0], 0.01)
    chase((240, 15, 3), (57, 3, 0))
    fade_out([240, 15, 3], 0.01)
    sparkle((255, 129, 0), (85, 78, 0))
