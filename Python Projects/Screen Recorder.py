from win32api import GetSystemMetrics
import cv2
import pyautogui
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width, height)

format_1 = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("Test.mp4", format_1, 30.0, dimension)

start_time = time.time()
duration = 10
end_time = start_time + duration

while True:
	image = pyautogui.screenshot()
	frame_1 = np.array(image)
	frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)

	output.write(frame)
	current_time = time.time()

	if current_time > end_time:
		break
output.release()
print("Recording Successfull")