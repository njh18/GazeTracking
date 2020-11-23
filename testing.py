# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:46:01 2020

@author: Jun Hso
"""

import cv2
from gaze_tracking import GazeTracking
import matplotlib.pyplot as plt
import time

cap = cv2.VideoCapture('B005.mp4')
gaze = GazeTracking()

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

mylist=[]
start_time=time.time()

#Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  now=time.time()
  
  if ret==True:
      # We send this frame to GazeTracking to analyze it
      gaze.refresh(frame)
    
      frame = gaze.annotated_frame()
      text = ""
    
      if gaze.is_blinking():
          text = "Blinking"
      elif gaze.is_right():
          text = "Looking right"
      elif gaze.is_left():
          text = "Looking left"
      elif gaze.is_center():
          text = "Looking center"
    
      cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    
      left_pupil = gaze.pupil_left_coords()
      right_pupil = gaze.pupil_right_coords()

      if left_pupil is None:
          pass
      else:
          mylist.append((left_pupil[0],left_pupil[1],now-start_time))
      
      cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
      cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
      cv2.putText(frame,"ratio: " + str(gaze.horizontal_ratio()),(90,195), cv2.FONT_HERSHEY_DUPLEX,0.9,(147,58,31),1)
    
    
      #cv2.imshow("Demo", frame)
      
      # Press Q on keyboard to  exit
      if cv2.waitKey(25) & 0xFF == ord('q'):
         break
     
  #break the loop
  else:
      break


# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()



x_coord=[]
y_coord=[]
timing=[]

normalx=mylist[0][0]
normaly=mylist[0][1]

for i in range(len(mylist)):
    x_coord.append(normalx-mylist[i][0])
    y_coord.append(normaly-mylist[i][1])
    timing.append(mylist[i][2])

print(x_coord)
print(y_coord)

plt.scatter(x_coord,y_coord,c=timing,cmap='RdPu_r')
    

