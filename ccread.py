from PIL import Image
import binascii
import argparse

class CryptCardReader(object):

	def __init__(self, image_file):

		self.image = Image.open(image_file)
		self.image_size = self.image.size
		self.pixel_data = self.image.load()
		self.pixel_num = self.image_size[0] * self.image_size[1]
		self.chunk_size = 8
		self.color_vals = {
			(255,255,255) : 0,
			(0,0,0) : 1
		}

		self.header_info()

	def header_info(self):

		byte = ''

		for ind in range(0, 8):

			byte += str(self.color_vals[(self.pixel_data[ind, 0])])

		self.message_size = int(byte, 2) + 1

	def read_pixel_data(self):

		x_val = 0
		y_val = 0

		bin_str = ''

		for pixel in range(0, self.pixel_num):

			if(x_val > (self.image_size[0] - 1)):

				x_val = 0
				y_val += 1

			#print("X Val : %s" % (x_val))
			#print("Y Val : %s" % (y_val))

			#print(str(self.retr_bin_vals(self.pixel_data[x_val, y_val])))

			bin_str += str(self.retr_bin_vals(self.pixel_data[x_val, y_val]))

			x_val += 1

		#print(self.bin_str)
		hidden_string = self.retr_hex_vals(bin_str)

		return hidden_string

	def retr_hex_vals(self, bin_val):

		bin_list = ([bin_val[i:i+self.chunk_size] for i in range(0, len(bin_val), self.chunk_size)]) # Understand what this line of code is doing?
		bin_list = bin_list[:self.message_size]
		ascii_chars = ''
		#print(bin_list)


		for byte in bin_list[1:]:

			byte_hex_val = hex(int(byte, 2)).replace('0x', '')
			
			if(len(byte_hex_val) < 2):

				byte_hex_val = ("%s%s" % ('0', byte_hex_val))

			ascii_chars += binascii.unhexlify(byte_hex_val)

		return ascii_chars



	def retr_bin_vals(self, rgb_val):

		return self.color_vals[rgb_val]


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="Specify the input file name")
	argument = parser.parse_args()

	application = CryptCardReader(argument.input)
	string = application.read_pixel_data()
	print(string)