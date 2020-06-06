#https://stackoverflow.com/questions/25349178/calculating-percentage-of-bounding-box-overlap-for-image-detector-evaluation

import numpy as np 
from shapely.geometry import Polygon
import matplotlib.pyplot as plt 
iou_framewise = []
iou_detect_track = []  



ftTLx = [] #framewise tested top left x values 
ftTLy = [] 	

ftTRx = []   
ftTRy = []

ftBRx = []
ftBRy = []

ftBLx = []
ftBLy = []


ctTLx = [] #coupling tested top left x values 
ctTLy = [] 	

ctTRx = []   
ctTRy = []

ctBRx = []
ctBRy = []

ctBLx = []
ctBLy = []


gTLx = [] #ground truth top left x values
gTLy = []

gTRx = []
gTRy = []

gBRx = []
gBRy = []

gBLx = []
gBLy = []

#gt values are in the format of xmin, ymax, ymin, xmax

#CHANGE HERE 
with open('framewise_coordinates.txt') as fp:   #read the coordinates of detected objects in test case 1 
	framewise_bb_values = [list(map(float, line.strip().split(' '))) for line in fp]

with open('ground_truth.txt') as fp1:           #read the coordinates of the ground truth 
	ground_truth_values = [list(map(int, line.strip().split(' '))) for line in fp1]

with open('detect_track_coordinates.txt') as fp2:  #read the coordinates of detected objects in test case 2
	detect_track_bb_values = [list(map(float, line.strip().split(' '))) for line in fp2]

#print(framewise_bb_values)


#framewise_bb_values 
#y values dont need to be subtracted from 720 as they are already in the correct coordinates 
#framewise_bb contains values in the form of 
#xmin,ymin, xmax,ymax

#assume (x1,y1) to be Bottom left corneR

#CHANGE HERE
#100 for occlusion scenarios   (since 100 frames have been annotated for the occlusion scenario) 
#otherwise 50                  (since 50 frames have been annotated for other scenarios) 
for i in range(100):
	ftTLx.append(framewise_bb_values[i][0]) 	#(x1,y1))
	ftTLy.append(framewise_bb_values[i][1])	

	ftTRx.append(framewise_bb_values[i][2]) 	#(x2,y1)
	ftTRy.append(framewise_bb_values[i][1])

	ftBRx.append(framewise_bb_values[i][2])	#(x2,y2)
	ftBRy.append(framewise_bb_values[i][3])	

	ftBLx.append(framewise_bb_values[i][0])	#(x1,y2)
	ftBLy.append(framewise_bb_values[i][3])	


#CHANGE HERE (occlusion)
for h in range(100):
	ctTLx.append(detect_track_bb_values[h][0]) 	#(x1,y1))
	ctTLy.append(detect_track_bb_values[h][1])	

	ctTRx.append(detect_track_bb_values[h][2]) 	#(x2,y1)
	ctTRy.append(detect_track_bb_values[h][1])

	ctBRx.append(detect_track_bb_values[h][2])	#(x2,y2)
	ctBRy.append(detect_track_bb_values[h][3])	

	ctBLx.append(detect_track_bb_values[h][0])	#(x1,y2)
	ctBLy.append(detect_track_bb_values[h][3])	


#gt_bb_values 
#y values dont have to be subtracted from 720 as the it is already adjusted in the ground truth code 
#gt_bb contains values in the form of 
#xmin, ymin, xmax, ymax 

#CHANGE HERE (occlusion)
for j in range(100):
	gTLx.append(ground_truth_values[j][0])	#(x1,y1))
	gTLy.append(ground_truth_values[j][3])
	

	gTRx.append(ground_truth_values[j][2])	#(x2,y1)
	gTRy.append(ground_truth_values[j][3])
	

	gBRx.append(ground_truth_values[j][2])	#(x2,y2)
	gBRy.append(ground_truth_values[j][1])
	

	gBLx.append(ground_truth_values[j][0])	#(x1,y2)
	gBLy.append(ground_truth_values[j][1])
	

iou_f = []
iou_c = [] 


def calculate_iou_framewise(box_1, box_2):  #iou calculator for test case 1 
	poly_1 = Polygon(box_1)
	poly_2 = Polygon(box_2)
	iou_f = poly_1.intersection(poly_2).area / poly_1.union(poly_2).area
	return iou_f

def calculate_iou_detect_track(box_3, box_2):  #iou calculator for test case 2 
	poly_3 = Polygon(box_3)
	poly_2 = Polygon(box_2)
	iou_c = poly_3.intersection(poly_2).area / poly_3.union(poly_2).area
	return iou_c

#CHANGE HERE(occlusion)
for k in range(100):
	box_1 = [[ftTLx[k], ftTLy[k]], [ftTRx[k], ftTRy[k]], [ftBRx[k], ftBRy[k]], [ftBLx[k], ftBLy[k]]]
	box_2 = [[gTLx[k], gTLy[k]], [gTRx[k], gTRy[k]], [gBRx[k], gBRy[k]], [gBLx[k], gBLy[k]]]
	if ground_truth_values[k] == [0,0,0,0] :
		#print(ground_truth_values[k][0],ground_truth_values[k][1] ,ground_truth_values[k][2] ,ground_truth_values[k][3]  )
		iou_framewise.append(0)
	else:
		iou_framewise.append(calculate_iou_framewise(box_1, box_2))

	#print(k)

#CHANGE HERE(occlusion)
for l in range(100):
	box_3 = [[ctTLx[l], ctTLy[l]], [ctTRx[l], ctTRy[l]], [ctBRx[l], ctBRy[l]], [ctBLx[l], ctBLy[l]]]
	box_2 = [[gTLx[l], gTLy[l]], [gTRx[l], gTRy[l]], [gBRx[l], gBRy[l]], [gBLx[l], gBLy[l]]]
	if ground_truth_values[l] == [0,0,0,0] :
		iou_detect_track.append(0)
	else:
		iou_detect_track.append(calculate_iou_detect_track(box_3, box_2))

#print(iou_framewise)
#print(iou_detect_track) 


#plot the variation of iou for both the test cases with the ground truth and draw conclusions 

plt.plot(np.linspace(0,100,100),iou_framewise,label='framewise',linestyle = '--',color='red')
plt.plot(np.linspace(0,100,100),iou_detect_track,label='detect and track',linestyle = '--',color='blue')
plt.plot(np.linspace(0,100,100),np.linspace(np.mean(iou_framewise),np.mean(iou_framewise),100),label='framewise mean',color='red')
plt.plot(np.linspace(0,100,100),np.linspace(np.mean(iou_detect_track),np.mean(iou_detect_track),100),label='detect and track mean',color='blue')

plt.legend(loc='best')
#plt.plot(np.linspace(0,50,50),'--b',iou_framewise)
#plt.plot(np.linspace(0,50,49),'--r',iou_detect_track)
plt.xticks(np.arange(0,101,5),rotation=90)
plt.yticks(np.arange(0, 1, 0.05))
plt.xlabel('frame number')
plt.ylabel('IoU')
#CHANGE HERE
plt.title('occlusion scenario')
plt.grid()

plt.show()





