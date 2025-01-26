'''
A srcipt to convert sanger sequencing data from a forward and reverse primer 
into a single unified sequence, given a specified degree of sequence overlap,
then optionally blast those sequences to a given subject sequence.

precondition: requires the forward and reverse sequences in .ab1 format (typically,
from sanger sequenceing) in positions 1 and two in the arguments in the command line,
respectively. Then optoinally provide the true argument to the -seperate 
flag if you want to keep the sequences seperated. Then optionally provide the name of the 
output file to store the consensus sequence of the two primer sequences in the argument 
with the -consensusSeq flag followed by the name for the file (without .fasta as the end) 
in the command line after thr first 3 reuired arguments. Finally an optional .fasta file 
of the sequence to align the consensus sequence to can be provided with the -subject 
flag in the command line after the first 3 required arguments are provided. 

postcondition: returns a .fasta file of the consensus sequence and a .txt file of the 
alignment of the consensus sequence to the porovided subject sequence. 
'''
#*********************************************************************

import sys
import os
import alignTwoSequences
import writeFASTA
import consensusSeq
import ab1Handler


if __name__ == '__main__':
	###### Collect info from user ##############################################
	# Check that first argument is .ab1 file type
	if sys.argv[1][-4:] == ".ab1":
		filename1 = sys.argv[1]
	else:
		print(f"{sys.argv[1]} is not a .ab1 file. " + 
		"Please provide .ab1 files in the first and second arguments " + 
		" after the program file in the command line.")
		sys.exit()

	# Check that second argument is .ab1 file type
	if sys.argv[2][-4:] == ".ab1":
		filename2 = sys.argv[2]
	else:
		print(f"{sys.argv[2]} is not a .ab1 file. " + 
		"Please provide .ab1 files in the first and second arguments " + 
		"after the program file in the command line.")
		sys.exit()

	# Assign the -seperate flag
	seperate = 'false'
	if "-seperate" in sys.argv:
		seperate_index = sys.argv.index("-seperate") + 1
		seperate = sys.argv[seperate_index]
	
	# check if a output file name is provided, asign consensusSeq if not
	outputfile = 'consensusSeq'
	if "-consensusSeq" in sys.argv:
		# Get the value following the flag
		outputfile_index = sys.argv.index("-consensusSeq") + 1
		outputfile = sys.argv[outputfile_index]

	# check if a subject file to blast against is provided
	subjectfile = None
	if "-subject" in sys.argv:
		# Get the index following the flag
		subjectfile_index = sys.argv.index("-subject") + 1
		# Check that there is an argument after the flag
		if subjectfile_index < len(sys.argv):
			# check that the argument after the -subject flag is a .fasta file
			if sys.argv[subjectfile_index][-6:] == ".fasta" or sys.argv[subjectfile_index][-3:] == ".fa":
				subjectfile = sys.argv[subjectfile_index]
			else:
				print(f"{sys.argv[subjectfile_index]} is not a .fasta file. " + 
				"Please provide a .fasta or .fa file after the -subject flag in the command line, " + 
				"or exclude the optional flag.")
				sys.exit()



	###### Plug user info into pipeline #############################################
	record1 = ab1Handler.read_ab1(filename1)
	record2 = ab1Handler.read_ab1(filename2)
	seq_1 = str(ab1Handler.base_calls(record1)).upper()
	seq_2 = str(ab1Handler.base_calls(record2).reverse_complement()).upper()
	consensusSequence = consensusSeq.consensusSeq(seq_1, seq_2)



	###### Return output to user ####################################################
	# If there is a matching overlap sequence and the seperate flag is not triggered, 
	# write the consensus sequence to a fasta file and align it to the given 
	# subject sequence. Otherwise write a fasta for each sequence and 
	# align each sequence individually if subject fasta is provided.
	seperate_flag_options = ["true", "True", "T", "t"]
	if len(consensusSequence) > 0 and (seperate not in seperate_flag_options):
		writeFASTA.write_fasta_file(consensusSequence, outputfile)
		print(f'The length of your consensus sequence is {len(consensusSequence)} bases.')
		if subjectfile:
			alignTwoSequences.align_Two_Seqs(f"{outputfile}.fasta", subjectfile, f"{outputfile}_aligned")
			print(f"Your new consensus sequence was aligned to {os.path.basename(subjectfile)}.")
	else:
		writeFASTA.write_fasta_file(seq_1, f"{outputfile}_forward_primer")
		print(f'The length of your forward primer sequence is {len(seq_1)} bases.')
		writeFASTA.write_fasta_file(seq_2, f"{outputfile}_reverse_primer")
		print(f'The length of your reverse primer sequence is {len(seq_2)} bases.')
		if subjectfile:
			alignTwoSequences.align_Two_Seqs(f"{outputfile}_forward_primer.fasta", subjectfile, f"{outputfile}_forward_primer_aligned")
			print(f"Your forward primer sequence was aligned to {os.path.basename(subjectfile)}.")
			alignTwoSequences.align_Two_Seqs(f"{outputfile}_reverse_primer.fasta", subjectfile, f"{outputfile}_reverse_primer_aligned")
			print(f"Your reverse primer sequence was aligned to {os.path.basename(subjectfile)}.")
	
	# inform user where results were placed
	current_directory = os.getcwd()
	if {os.path.dirname(outputfile)} == '':
		print(f"See folder {os.path.basename(current_directory)} for results.")
	else:
		print(f"See folder {os.path.dirname(outputfile)} for results.")