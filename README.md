# Research-Development
This repository contains the description of my Research &amp; Development project.<br> 

The repository has the following structure: <br>
(i) contemporary research papers  <br> 
- per frame methodologies <br> 
- temporal information methodologies <br> 

(ii) custom data  <br>
-decomposed_input_video: contains the frames comprising the input videos <br>
-ground_truth_annotation: manually annotated frames obtained using annotation.py <br> 
-input_video: contains the test input video <br> 

(iii) output <br>
-decomposed_output_video: 
	-coupled: contains frames decomposed from the output video of coupled approach  <br> 
	-framewise: contains frames decomposed from the output video of framewise approach <br> 
-detected_coordinates.txt: contains the bounding boxes coordinates of detected approach object for both approaches <br> 
fps_count: frame per second count readings for both methods <br> 
-inference_times: contains the timings required for both approaches to process the video <br> 
output_video: contains the video output of both approaches <br> 
-iou_scissor_om.png: comparison of IoU for both approaches for a given input <br>
-it_scissor_om.png: comparison of inference times for both approaches for a given input <br> 

(iv) src <br> 
-annotation.py: script to annotate the video inputs and generate annotated frames <br> 
-coupled_dt_28_11_2019.ipynb: pipeline implementing Coupled approach <br> 
-Fragmenting_videos_to_frames.py: decomposing video inputs to constituent frames <br> 
-framewise_28_11_2019.ipynb: pipeline implementing Framewise approach <br> 
-inference_time_comparison.py: script to compare the inference times for both approach and generate a plot 
-iou_calculator.py: script to compare the IoU for both approaches with ground truth and generate a plot 
-object_detection_tutorial_video_webcam.py: test webcam working with tensorflow api 


