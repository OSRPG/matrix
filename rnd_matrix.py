#!/usr/bin/env python
# coding: utf8

def read_permanence(permanence_file_name, max_coups):		        	### a function to read and import a permanence file
	try: perm_file_handle = open(permanence_file_name,'r')			# try to open the file, relative to the path of this script file, to read
	except: return(-1)							# error: could not read the file

	permanence=[]								# create empty permanence variable, of type "list"
	current_length = 0

	for line in perm_file_handle:						# walk through the file, line by line
		if current_length >= max_coups: break		        	# stop reading the file
		line = str.split( str(line).replace(',',' ') )			# split multiple patterns in the line and remove commas

		for piece in line:						# walk through the pieces
			if current_length >= max_coups: break			# stop reading the file
			
			if piece.isdigit() and len(piece) < 3:			# check for digit and length
				try: num_piece = int(piece)			# try to convert to integer
				except: continue				# on error, skip this piece

				if num_piece >= 0 and num_piece <= 36: 		# we use numbers from 0 to 36, no 00 here
					permanence.append(num_piece)		# add the number to the permanence variable
					current_length += 1					# count this number

	perm_file_handle.close()						# close the permanence file

	if len(permanence) == 0: return(-2)					# error: permanence has no numbers
	else: return(permanence)						# give back the new permanence


def main(): 									# where the programme really starts
	from sys import argv					        	# library function to show the given command itself
	import getopt								# library function for command line options

	opts, args = getopt.getopt(argv[1:], "hp:n:")	                        # defines possible command line options
	random = True								# set the random flag variable on true as default
	max_coups = 37*37				                	# set rotation² as default value
	permanence = []					                	# empty list variable

	for o, a in opts:					        	# iterate through given options
		if o == "-h": print argv[0],"\n -h help, this page\n -p permanence filename, else random numbers will be used\n -n amount of numbers\n"; exit(0)	# shows help text
		if o == "-p": permanence_file_name = str(a); random = False
		if o == "-n": max_coups = int(a)		                # if given, set variable

	if not random:								# a file name is given
		permanence = read_permanence(permanence_file_name, max_coups)	# fill the variable by reading the file with the read function
		if  max_coups > len(permanence):
			max_coups = len(permanence)				# reset max coups if to big

	else:									# use the PRNG
		from random import randint					# lib function giving integers
		permanence_file_name = "PRNG"
		for i in range(0,max_coups): 					# loop max_coups times
			permanence.append( randint(0,36) )			# append a random number to the perm variable

	if permanence == -1: 
		print "ERROR: can not read the file:",permanence_file_name	# give error message
		return(1)							# leave the programme
	elif permanence == -2: 
		print "ERROR:",permanence_file_name,"contains no useable numbers"
		return(1)

	for number in permanence:						# walk through the permanence variable
		print str(number)+',',						# print the number to the screen, with commas, no newline

	print ''								# end the last line
	print max_coups,"numbers from",permanence_file_name	        	# print a summary

	return(0)								# regular end of the programme


main()										# call the main function to run
