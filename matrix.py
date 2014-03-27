#!/usr/bin/env python
# coding: utf8

def read_permanence(permanence_file_name):					### a function to read and import a permanence file
	try: perm_file_handle = open(permanence_file_name,'r')			# try to open the file, relative to the path of this script file, to read
	except: return(-1)							# error: could not read the file
	
	permanence=[]								# create empty permanence variable, of type "list"
	
	for line in perm_file_handle:						# walk through the file, line by line
		line = str.split( str(line).replace(',',' ') )			# split multiple patterns in the line and remove commas
		
		for piece in line:						# walk through the pieces
			if piece.isdigit() and len(piece) < 3:			# check for digit and length
				try: num_piece = int(piece)			# try to convert to integer
				except: continue				# on error, skip this piece
				
				if num_piece >= 0 and num_piece <= 36: 		# we use numbers from 0 to 36, no 00 here
					permanence.append(num_piece)		# add the number to the permanence variable
	
	perm_file_handle.close()						# close the permanence file
	
	if len(permanence) == 0: return(-2)					# error: permanence has no numbers
	else: return(permanence)						# give back the new permanence


def main(): 									# where the programme really starts
	permanence_file_name = "permanence.txt"					# string variable with the file name
	permanence = read_permanence(permanence_file_name)			# fill the variable by reading the file with the function
	
	if permanence == -1: 
		print "ERROR: can not read the file:",permanence_file_name	# give error message
		return(1)							# leave the programme
	elif permanence == -2: 
		print "ERROR:",permanence_file_name,"contains no useable numbers"
		return(1)
	
	for number in permanence:						# walk through the permanence variable
		print number,',',						# print the number to the screen, with commas, no newline
	
	print ''								# end the line
	print len(permanence),"numbers in",permanence_file_name			# print a summary
	
	return(0)								# regular end of the programme


main()										# call the main function to run
