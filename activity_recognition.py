import numpy as np
import argparse
import imutils
import sys
import cv2

#define the sample duration (i.e., # of frames for classification) and sample size
# (i.e., the spatial dimensions of the frame)
SAMPLE_DURATION = 16
SAMPLE_SIZE = 112


# grab a pointer to the input video stream
print("[INFO] accessing video stream...")
vs = cv2.VideoCapture(0)

# loop until we explicitly break from it
while True:
	# initialize the batch of frames that will be passed through the
	# model
	frames = []

	# loop over the number of required sample frames
	for i in range(0, SAMPLE_DURATION):
		# read a frame from the video stream
		(grabbed, frame) = vs.read()

		# if the frame was not grabbed then we've reached the end of
		# the video stream so exit the script
		if not grabbed:
			print("[INFO] no frame read from stream - exiting")
			sys.exit(0)

		# otherwise, the frame was read so resize it and add it to
		# our frames list
		frame = imutils.resize(frame, width=600)
		frames.append(frame)

	# now that our frames array is filled we can construct our blob
	blob = cv2.dnn.blobFromImages(frames, 1.0,
		(SAMPLE_SIZE, SAMPLE_SIZE), (114.7748, 107.7354, 99.4750),
		swapRB=True, crop=True)
	blob = np.transpose(blob, (1, 0, 2, 3))
	blob = np.expand_dims(blob, axis=0)



	# loop over our frames
	for frame in frames:
	
		# display the frame to our screen
		cv2.imshow("Activity Recognition", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

vs.release()
cv2.destroyAllWindows()