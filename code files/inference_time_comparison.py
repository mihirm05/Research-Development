import matplotlib.pyplot as plt 
import numpy as np 

#CHANGE HERE
f_time = open("/framewise_time.txt","r")          #read the time needed for test scenario 1 (stored earlier after detection)
dt_time = open("/detect_track_time.txt","r")      #read the time needed for test scenario 2 (stored earlier after detection)   

framewise_time_cleaned = []  #this list stores the time values which neglect the spurious readings for test scenario 1 
detect_track_time_cleaned = [] #this list stores the time values which neglect the spurious readings for test sceario 2 

#load framewise track times in a list 
framewise_time = f_time.read().split() 
framewise_time = [float(framewise_time[i]) for i in range(len(framewise_time))]
#print(framewise_time)
for i in range(len(framewise_time)):
	if framewise_time[i] < 160:
		framewise_time_cleaned.append(framewise_time[i])

#print(len(framewise_time_cleaned))

#load detect track times in a list 
detect_track_time = dt_time.read().split()
detect_track_time = [float(detect_track_time[j]) for j in range(len(detect_track_time))]
for i in range(len(detect_track_time)):
	if detect_track_time[i] < 160:
		detect_track_time_cleaned.append(detect_track_time[i])
print(len(detect_track_time_cleaned))

#print(np.max(framewise_time[1:] + detect_track_time[1:]))
#print(detect_track_time[1:])
#print(np.max(int(np.max(framewise_time[1:])),int(np.max(detect_track_time[1:]))))


#plot the readings and visualise the results

plt.plot(np.linspace(0,100,len(framewise_time_cleaned)),framewise_time_cleaned[:],'--r',label='framewise detections')
plt.plot(np.linspace(0,100,len(detect_track_time_cleaned)),detect_track_time_cleaned[:],'--b',label='detect and track')
plt.plot(np.linspace(0,100,len(framewise_time_cleaned)),np.linspace(np.mean(framewise_time_cleaned[:]),np.mean(framewise_time_cleaned[:]),len(framewise_time_cleaned)),'r',label='framewise mean')
plt.plot(np.linspace(0,100,len(detect_track_time_cleaned)),np.linspace(np.mean(detect_track_time_cleaned[:]),np.mean(detect_track_time_cleaned[:]),len(detect_track_time_cleaned)),'b',label='detect and track mean')
plt.grid()
plt.xticks(np.arange(0, 100, step=5),rotation = 90)
plt.yticks(np.arange(0, np.max(framewise_time_cleaned[:] + detect_track_time_cleaned[:]),step =5))

plt.xlabel('frame number')
plt.ylabel('time (ms)')
plt.legend(loc='best')
#change here 
plt.title('cluttered scenario')
#plt.plot(np.linspace(0,50,50),dt_time)
plt.show()

