"""Writes a .fasta file."""
import os

def write_fasta_file(sequence, sequence_name):
	'''
	Generate fasta file to compare sequences to original plasmid.
	precondition:reuires a sequence as a string oject and a name for
	the sequence as a string object. The name can be a directory path
	with the basename being the name for the file.
	psotcondition: returns a fasta file of the seuqence.
	'''
	fasta_lines = []
	line = ''
	i = 0
	for char in sequence:
		line += char
		if len(line) == 50:
			fasta_lines.append(line + f'\n')
			line = ''
		elif i == len(sequence)-1:
			fasta_lines.append(line + f'\n')
		i += 1
	fasta_lines.insert(0, f'>{os.path.basename(sequence_name)}\n')
	
	fasta_file = open(f'{sequence_name}.fasta', 'w')
	fasta_file.writelines(fasta_lines)
	fasta_file.close()	