import sys 
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')    #this line is useful in cases when ros and cv have conflict
import cv2
#sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

path = ' '  #add custom path 

#CHANGE HERE   
vidcap = cv2.VideoCapture(path + 'mp.mp4') #path to video file

success,image = vidcap.read()
count = 1
while success:
	#CHANGE HERE 
	cv2.imwrite(path + 'Cup/%d.jpg' % count, image)     # save frame as JPEG file      

	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1
	if count == 50:
		break
	print(count)
	if count == int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)):
		break
