"""Finds all consecutive matching sub-equences in two sequences."""

def find_Matching_Sequences(subSeq1, subSeq2):
	'''
	Find all matching consecutive subsequences within two sequences of equal length.
	Helper function for align_sequences().
	precondition: takes two sequences as strings of equal length
	postcondition: returns a list of the lengths of the matching subsequences.
	'''
	matches = []
	subSeq = ''
	for i in range(0, len(subSeq1)):
		if subSeq1[i].lower() == subSeq2[i].lower():
			subSeq = subSeq + subSeq1[i]
			if len(subSeq1) == 1:
				matches.append(subSeq)
		else:
			matches.append(subSeq)
			subSeq = ''
	return matches