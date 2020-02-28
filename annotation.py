# import the necessary packages
#https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

import glob
import sys 
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

 
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not

refPt = []
cropping = False
path = '/home/mihir/Desktop/R&D/Implementation_Practice/FINAL TESTS/'

#CHANGE HERE
ground_truth = open(path + "Scissor_oc/ground_truth.txt", 'w')

#CHANGE HERE
vidcap = cv2.VideoCapture(path + 'Scissor_oc/oc.mp4') 

success,image = vidcap.read()
count = 0
while success:
	#CHANGE HERE 
	cv2.imwrite(path + 'Scissor_oc/%d.jpg' % count, image)     # save frame as JPEG file      

	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1
	if count == 100:
		break
	print(count)
	if count == int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)):
		break


def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		
		refPt = [(x, y)]
		cropping = True
		
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		 
		refPt.append((x, y))
	
		# draw a rectangle around the region of interest
		cv2.rectangle(images, refPt[0], refPt[1], (0, 255, 0), 2)
		#print(refPt[0],refPt[1])
		
		sys.stdout = ground_truth
     
        #xmin,ymax,xmax,ymin
        #print(refPt[0][0],refPt[0][1],refPt[1][0],refPt[1][1])

		#xmin,ymin,xmax,ymax
		print(refPt[0][0],refPt[1][1],refPt[1][0],refPt[0][1])
		
		#ymin,xmin,ymax,xmax
		#print(refPt[0][1],refPt[0][0],refPt[1][1],refPt[1][0])
		#f.close()
		cv2.imshow("image", images)

		#CHANGE HERE
		cv2.imwrite(path + "Scissor_oc/gt"+str(i)+".jpg", images)




#cv2.imshow('object',images[1])
# load the image, clone it, and setup the mouse callback function

i = 0
while i <= 100:
	#CHANGE HERE
	images = cv2.imread(path + "Scissor_oc/"+str(i)+".jpg")
	#images = cv2.imread("/home/mihir/Desktop/R&D/Implementation_Practice/Videos_short/Scissor/mp.mp4")
	#print('frame number is: ',i)
	clone = images.copy()
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", click_and_crop)
	#font = cv2.FONT_HERSHEY_SIMPLEX
    

	# display the image and wait for a keypress
	cv2.imshow("image", images)
	#cv2.putText(images[i],'OpenCV',(10,500), font, 10,(255,255,255),2,cv2.LINE_AA)
	
	key = cv2.waitKey(7000) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
 
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break
	i += 1 
# if there are two reference points, then crop the region of interest
# from teh image and display it
#if len(refPt) == 2:
#	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
#	cv2.imshow("ROI", roi)
#	cv2.waitKey(0)
#f.close()
## close all open windows
#cv2.destroyAllWindows()



