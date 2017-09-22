import time 
from datetime import datetime

#Class Buffer with only data
class RingBuffer(object):

	def __init__(self, size):
		self.size = size
		self.data = [None for i in range(0, size)]
		self.index = 0

	#Insert a new item in the buffer
	def append(self, item):
		self.data[self.index] = item
		self.index = self.index + 1

		if self.index == self.size:
			self.index = 0

	#Print the buffer
	def printBuffer(self):
		for i in range(0,self.size):
			print("%s" % (self.data[i]))
	
	#Return the data buffer
	def get(self):
		return self.data

	#Return True or False if there are any none position
	def ready(self):
		return any(i != None for i in self.data)

	#Return the index position of the buffer
	def getPos(self):
		return self.index

	#Return the lastest data inserted
	def getLastData(self):
		return self.data[self.index-1]

	#Clear de buffer data
	def clearBuffer(self):
		self.data = [None for i in range(0, self.size)]

#Class Buffer with data and timestamp
class RingBufferTS(object):

	def __init__(self, size):
		self.size = size
		self.data = [None for i in range(0, size)]
		self.ts = [None for i in range(0, size)]
		self.index = 0

	#Insert a new item and a new timestamp in the buffer
	def append(self, item):
		self.ts[self.index] = datetime.now().strftime('%H:%M:%S')
		self.data[self.index] = item
		self.index = self.index + 1

		if self.index == self.size:
			self.index = 0

	#Print the buffer with data and timestamp
	def printBuffer(self):
		for i in range(0,self.size):
			print("%s , %s " % (self.data[i],self.ts[i]))
	
	#Return the data and timestamp buffer
	def get(self):
		return self.data , self.ts

	#Return the index position of the buffer
	def getPos(self):
		return self.index

	#Return the lastest data and timestamp inserted
	def getLastData(self):
		return self.data[self.index-1], self.ts[self.index-1]

	#Clear de buffer data and timestamp
	def clearBuffer(self):
		self.data = [None for i in range(0, self.size)]
		self.ts = [None for i in range(0, self.size)]

def main():
	size = 10
	partial = 5

	#print(datetime.now())

	#Create the Buffer
	buffer = RingBufferTS(size)

	#fill the buffer
	for x in range (0,size):
		buffer.append(x+1)
		time.sleep(0.2)

	#Get all buffer (data and timestamp)
	data, ts = buffer.get()

	#print the buffers
	buffer.printBuffer()

	#get the index position of buffer
	print("Pos index: %d" % (buffer.getPos()))

	#get the lastData in buffer
	data , ts = buffer.getLastData()

	#Print the lastItem
	print("Last item: %s , %s" % (data,ts))

	#Clear the buffer
	buffer.clearBuffer()

	#Print buffer
	buffer.printBuffer()

if __name__ == "__main__":
    main()


