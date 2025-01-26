"""Constructs a consensus sequence from two parent sequences."""
import maxMatchingSubSeq

def consensusSeq(seq1, seq2):
	'''
	Find indices of each sequence around matching sub-sequence
	and combine them into one continuious sequence. Uses align_sequences()
	precondition: requires two sequences and a matching sub-sequence 
	postcondition: returns the compiled sequence or returns integer -1 if there is 
	no consensus sequence.
	'''
	matchingSeq = maxMatchingSubSeq.maximum_Match(seq1, seq2)
	
	try:
		if len(matchingSeq) > 0:
			seq1StopIndex = seq1.find(matchingSeq)
			seq2StartIndex = seq2.find(matchingSeq)
			consensusSeq = seq1[:seq1StopIndex] + seq2[seq2StartIndex:]
			return consensusSeq
		else:
			return ''
	except TypeError:
		return -1
