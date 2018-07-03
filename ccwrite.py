from PIL import Image
import argparse


class CryptCard(object):

	def __init__(self, width, height, img_name):

		self.intense = 255
		self.pixel_vals = [(255,255,255), (0,0,0)]
		self.width = width
		self.height = height
		self.img_name = img_name
		self.img = Image.new('RGB', (self.width, self.height))

	def toHex(self, text):

		hexList = []

		for char in text:

			asciihex = hex(ord(char)).replace('0x', '')
			hexList.append(asciihex)

		return hexList
			

	def toBin(self, hex_val, decimal_conv=False):

		self.hex_val = hex_val

		if (decimal_conv):

			self.scale = 10

		else:
			self.scale = 16 ## equals to hexadecimal

		self.bitNum = 8

		return bin(int(self.hex_val, self.scale))[2:].zfill(self.bitNum) # LOOK INTO zfill METHOD!!!


	def convert_text(self, text):

		self.text = text

	def gen_bin_list(self, text):

		binList = []

		#text = ("%s%s" % (str(len(text)), text))
		#print(self.toBin("20", False))

		mess_len_b10 = len(text)
		mess_len_b16 = hex(mess_len_b10).split('x')[-1]
		
		if(len(mess_len_b16) < 2):

			mess_len_b16 = ("%s%s" % (0, mess_len_b16))

		binList.append(self.toBin(mess_len_b16))

		for hex_value in self.toHex(text):

			binList.append(self.toBin(hex_value))

		return binList

	def gen_pixel_list(self, bin_list):

		self.pixel_list = []
		self.iterator = 0
		self.pixel_num = self.width * self.height
		#print(self.pixel_num)

		for pixel in range(self.pixel_num):

			for byte in bin_list:

				#print(byte)

				for bit in byte:

					if(len(self.pixel_list) < self.pixel_num):

						if(int(bit)):
							self.pixel_list.append(self.pixel_vals[1])
							self.iterator += 1

						else:
							self.pixel_list.append(self.pixel_vals[0])
							self.iterator += 1

			#if (self.iterator == 2):
			#	self.iterator = 0

			#print(self.pixel_vals[self.iterator])
			#self.pixel_list.append(self.pixel_vals[self.iterator])

			#self.iterator += 1
			#print(self.iterator/8)
			#print(len(self.pixel_list))

		#print(self.pixel_list)


	def gen_image(self):

		self.img.putdata(self.pixel_list)
		self.img.save(self.img_name)

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("output", help="Specify the output file name")
	parser.add_argument("text", help="Specify text for rastorization process")
	arguments = parser.parse_args()

	print(arguments.output)

	application = CryptCard(200, 200, arguments.output)
	binData = application.gen_bin_list(arguments.text)
	application.gen_pixel_list(binData)
	application.gen_image()
