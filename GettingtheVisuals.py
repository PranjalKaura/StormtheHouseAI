import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from mss import mss 
import math
from directKeys import click, queryMousePosition, PressKey, ReleaseKey, SPACE

previous_clicks = []
startx = 577
starty = 709
clipSize = 0



# Faster_Algo_FirstCLick()


              
def Print_MousePos(original_image):
    print("pos", pyautogui.position()) 
    print(original_image.pixel(pyautogui.position().x-577, pyautogui.position().y - 281))
    time.sleep(1)

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def upgradeGun():
	print("entered Buy area")
	
	for i in range(0,5):

		pyautogui.click(661, 553)
		time.sleep(0.4)
	pyautogui.click(893, 915)


def screen_record(): 
	bulletsFired = 1
	clipSize = 6
	while(True):
		image =  np.array(ImageGrab.grab(bbox=(startx,starty,1200,958)))
		original_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		cv2.imshow("origi", original_image)
		print("brown ", original_image[761 - starty, 649 - startx])
		if original_image[761 - starty, 649 - startx] > 180 :
			time.sleep(3)
			upgradeGun()
			clipSize+=3
			time.sleep(3)

		for cordsy in range(1,original_image.shape[0], 2):
					for cordsx in range(1,original_image.shape[1], 2):
						if original_image[cordsy][cordsx] < 5:
							max_previous_click_length = 5
							click_bubble_range = 50
							too_close = False
							for pos in previous_clicks:
								if dist(cordsx + startx, cordsy+ starty, pos[0], pos[1]) < click_bubble_range:
									too_close = True
									break
							if too_close:
								continue
							print("Clicked ", cordsx, cordsy)
							pyautogui.click(cordsx + startx + 10, cordsy + starty, 2)
							bulletsFired+=2
							previous_clicks.append([cordsx +startx, cordsy+ starty])
							if len(previous_clicks) > max_previous_click_length:
								del previous_clicks[0]
							if bulletsFired>clipSize:
								PressKey(SPACE)
								time.sleep(0.05)
								bulletsFired = 1
								ReleaseKey(SPACE)
							break

		
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

time.sleep(6)
last_time = time.time()
screen_record()

