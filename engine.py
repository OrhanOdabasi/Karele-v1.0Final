#!/usr/bin/env python3

import random
import ast

class Engine:

	# Creating and filling the square
	def __init__(self, n):

		# Let's create a n*n square.
		self.n = n
		self.matrix = []
		for every in range(self.n):
			matrix_row = []
			for every in range(n):
				matrix_row.append(None)
			self.matrix.append(matrix_row)
		
		
		# generating two numbers and making this point as starting point
		self.number = 1
		x = random.randint(0, self.n-1)
		y = random.randint(0, self.n-1)
		
		self.matrix[x][y] = self.number		
		self.first_x = x
		self.first_y = y

		
		loop = True	

		while loop == True:

			# possible options are being generated
			self.option = ""
			if (y+3) <= (self.n-1) and self.matrix[x][y+3] == None:
					self.option += "a"	
			if (x-2) >= 0 and (y+2) <= (self.n-1) and self.matrix[x-2][y+2] == None:
					self.option += "b"
			if (x-3) >= 0 and self.matrix[x-3][y] == None:
					self.option += "c"
			if (x-2) >= 0 and (y-2) >= 0 and self.matrix[x-2][y-2] == None:
					self.option += "d"
			if (y-3) >= 0 and self.matrix[x][y-3] == None:
					self.option += "e"
			if (x+2) <= (self.n-1) and (y-2) >= 0 and self.matrix[x+2][y-2] == None:
					self.option += "f"
			if (x+3) <= (self.n-1) and self.matrix[x+3][y] == None:
					self.option += "g"
			if (x+2) <= (self.n-1) and (y+2) <= (self.n-1) and self.matrix[x+2][y+2] == None:
					self.option += "h"


			if self.option != "":
				
				# choosing a random option to continue
				road = random.choice(self.option)
								
				self.number += 1
				if road == "a":					
					y = y+3
					self.matrix[x][y] = self.number
					
				if road == "b":					
					x = x-2
					y = y+2
					self.matrix[x][y] = self.number
					
				if road == "c":					
					x = x-3
					self.matrix[x][y] = self.number
					
				if road == "d":					
					x = x-2
					y = y-2
					self.matrix[x][y] = self.number
					
				if road == "e":					
					y = y-3
					self.matrix[x][y] = self.number
					
				if road == "f":					
					x = x+2
					y = y-2
					self.matrix[x][y] = self.number
					
				if road == "g":					
					x = x+3
					self.matrix[x][y] = self.number
					
				if road == "h":					
					x = x+2
					y = y+2
					self.matrix[x][y] = self.number
					
				loop = True
				

			else:			
				if self.number == self.n * self.n:
					print("YOU'RE SO LUCKY!!! THE SQUARE HAS BEEN FILLED COMPLETELY!!!")
				else:
					print("Trying to fill... (Press 'Ctrl + C' to terminate the process.)")
				loop = False
		
		
	# reporting the result - returns a string
	def report(self):
		ln0 = "-" * 70 + "\n"
		ln1 = ":::::::REPORT:::::::\n"
		ln2 = "-" * 70 + "\n"
		ln3 = str(self.number) + " numbers has been placed to " + str(self.n) + "*" + str(self.n) + "-sized square!!!\n"
		ln4 = "First number has been placed in matrix[" + str(self.first_x) + "][" + str(self.first_y) + "] coordinates.\n"
		ln6 = ""
		for every in range(self.n):
			matrixln = self.matrix[every]
			ln5 = str(matrixln) + "\n"
			ln6 = ln6 + ln5		
		report = ln0 + ln1 + ln2 + ln3 + ln4 + ln6
		return report

	# saving the report into a document (*.txt file)
	def saveReport(self, report):

		file_name = "report" + str(self.n) + ".txt"
		saving = open(file_name, "a")
		saving.write(report + "\n")
		saving.close()

	# final number that the script reached to
	def finalNumber(self):

		return self.number
