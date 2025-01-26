"""Finds the longest consecutive subsequence from two parent sequences
and returns the subsequence. Requires consecutiveSeqs.py"""
import consecutiveSeqs


def maximum_Match(seq_1, seq_2):
	'''
	Finds largest matching sub sequence with two sequences, returns the sequence.
	Requires consecutiveSeqs.py to be imported
	precondition: requires two sequences as strings and an a threeshold as
	an integer that indicates the minimum the matching sequence must be.
	postcondition:Returns the maximum overlapping sequence.
	'''
	longerSeq = ''
	shorterSeq = ''
	if len(seq_1) > len(seq_2):
		longerSeq = seq_1
		shorterSeq = seq_2
	else:
		longerSeq = seq_2
		shorterSeq = seq_1
	
    # determine number of interations
	iterations = len(longerSeq) + len(shorterSeq) - 1
	longerSeqSlice_StartIndex = 0
	longerSeqSlice_EndIndex = 0
	shorterSeqSlice_StartIndex = len(shorterSeq) -1
	shorterSeqSlice_EndIndex = len(shorterSeq) -1
	maxMatches = []
	for i in range(0, iterations):
		longerSeq_slice = longerSeq[longerSeqSlice_StartIndex:longerSeqSlice_EndIndex + 1]
		shorterSeq_slice = shorterSeq[shorterSeqSlice_StartIndex:shorterSeqSlice_EndIndex + 1]
		matches = consecutiveSeqs.find_Matching_Sequences(longerSeq_slice, shorterSeq_slice)
		maxMatch = max(matches, key=len)
		maxMatches.append(maxMatch)
		
		if longerSeqSlice_EndIndex < len(longerSeq) - 1:
			longerSeqSlice_EndIndex += 1
		elif (longerSeqSlice_EndIndex == len(longerSeq) - 1):
			longerSeqSlice_StartIndex += 1
			
		if shorterSeqSlice_StartIndex > 0:
			shorterSeqSlice_StartIndex -= 1

		if (shorterSeqSlice_EndIndex - shorterSeqSlice_StartIndex > longerSeqSlice_EndIndex - longerSeqSlice_StartIndex):
			shorterSeqSlice_EndIndex -= 1
			
		if (longerSeqSlice_EndIndex - longerSeqSlice_StartIndex > shorterSeqSlice_EndIndex - shorterSeqSlice_StartIndex):
			longerSeqSlice_StartIndex += 1
			
		i += 1
	#print(f"maxMatches from maximum_Match(): {maxMatches}")
	maximumMatch = max(maxMatches, key=len)
	print(f"Your largest overlapping sequence is {len(maximumMatch)}bp: 5`{maximumMatch} ")
	if len(maximumMatch) > 0:
		return maximumMatch
	else:
		print("These seuences could not be aligned.")
		return ''

