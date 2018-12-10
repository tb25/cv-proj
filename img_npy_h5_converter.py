"""

	Author: Kevin Jiang

"""

import numpy as np
import h5py
import cv2
import sys

class ImageDataConverter():
	def __init__(self):
		try:
			self.input_filename = sys.argv[1]
			self.output_filename = sys.argv[2]
			self.input_format = sys.argv[3]
			self.output_format = sys.argv[4]
		except:
			error("Usage: main.py <input path> <output path> <input format> <output format>")

		print("INFO: Converting {} to {}.".format(self.input_format, self.output_format))

		try:
			if self.input_format == "img":
				output_npy = cv2.imread(self.input_filename, 0)
				if self.output_format == "npy":
					np.save(self.output_filename, output_npy)
				elif self.output_format == "h5":
					self.write_h5()

			if self.input_format == "npy":
				if self.output_format == "img":
					self.write_img()
				elif self.output_format == "h5":
					self.write_h5()

			if self.input_format == "h5":
				if self.output_format == "img":
					self.write_img()
				elif self.output_format == "npy":
					self.write_npy()
		except:
			error("Conversion error.")

	# Expects h5 or img, writes npy
	def write_npy(self):
		hf = h5py.File(self.input_filename, "r")
		datasets = hf.keys()
		count = 0
		for dataset in datasets:
			data_np = np.array(hf.get(dataset), dtype=np.uint8)
			np.save("{}{}".format(self.output_filename, count), data_np)
			count += 1

			print("INFO: Writing {}{}".format(self.output_filename, count))
		hf.close()

	# Expects npy or h5, writes img
	def write_img(self):
		if self.input_format == 'npy':
			output_img = np.load(self.input_filename)
			cv2.imwrite(self.output_filename, output_img)
		elif self.input_format == 'h5':
			hf = h5py.File(self.input_filename, "r")
			datasets = hf.keys()
			for dataset in datasets:
				data_np = np.array(hf.get(dataset))
				cv2.imwrite(self.output_filename, data_np)
			hf.close()

		print("INFO: Writing {}.".format(self.output_filename))

	# Expects npy or img, writes h5
	def write_h5(self):
		if self.input_format == "npy":
			input_np = np.load(self.input_filename)
		elif self.input_format == "img":
			input_np = cv2.imread(self.input_filename)
		hf = h5py.File(self.output_filename, "w")
		hf.create_dataset(self.output_filename, data=input_np)

		print("INFO: Writing {}.".format(self.output_filename))
		hf.close()
		#elif self.input_format == "img":			

if __name__ == "__main__":
	converter = ImageDataConverter()
