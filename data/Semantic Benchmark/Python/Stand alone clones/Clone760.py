def main() :
	cap = VideoCapture()
	shape = cap.get_size()
	shared_array_base = Array(ctypes.c_uint8, shape [0] * shape [1] * shape [2])
	frame = np.ctypeslib.as_array(shared_array_base.get_obj())
	frame = frame.reshape(shape [0], shape [1], shape [2])
	finished = Value('i', 0)
	video_process = Process(target = stream,
	args = (cap, shared_array_base, finished))
	video_process.start()
	time.sleep(2)
	def terminate() :
		print ("Main: termination")
		finished.value = True
		time.sleep(1)
		video_process.join()
	while True :
		try :
			cv2.imshow('frame', frame)
			time.sleep(0.1)
			cv2.waitKey(1)
		except KeyboardInterrupt :
			cv2.destroyAllWindows()
			terminate()
			break


def main() :
	reader, writer = multiprocessing.Pipe(False)
	video_process = Process(target = capture_video, args = [writer])
	video_process.start()
	while True :
		try :
			frame = reader.recv()
			process_frame(frame)
		except KeyboardInterrupt :
			video_process.terminate()
			break

