#!/usr/bin/env python3

#############################################################
# Script Name: Karele v1.0 Final
# Author: Orhan Odabaşı
# Date: 16th September 2014
# Contact Me: google.com/+OrhanOdabaşı
# About: It's a python 3 script which simulates 
# a game based on filling a n*n square with
# consecutive numbers from 1 to n by keeping up
# the following rules:
# - 2 spaces between the horizontal or vertical moves
# - 1 space between the diagonal moves
# The script does not guarantee to fill all the cells,
# it only fills them within orders randomly.
# For More Info: http://0rhodabasi.blogspot.com.tr/ (Turkish)
#############################################################


from engine import *
import time

loop = True

square_number = 5 # change the number as you wish, but consider that the more you set higher numbers, the more it takes time
count = 0

while loop == True:

	obj = Engine(square_number)
	number = obj.finalNumber()
	count += 1

	if number == square_number ** 2:

		loop = False
		report = obj.report()
		print(report)
		process_time = format(time.process_time(), ".2f")
		message = "Process was completed after "+ str(count) + " tries in " + process_time + " seconds!\n"
		message1 = "_" * 70 + "\n"
		print(message + message1)
		obj.saveReport(report + message + message1 + message1 )
