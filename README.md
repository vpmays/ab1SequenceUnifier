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