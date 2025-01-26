'''
Script to use blastn to align two sequences.

precondition: requires two fasta files for the query and subject sequences and 
a name for the output file (not including the .txt extension).
postcondition: returns a text file containg the results of the blast
'''
import os

# use blastn to align sequences and save the output
def align_Two_Seqs(query, subject, out):
    '''
    precondition: accepts strings of the fasta files with .fasta included in name 
    to align and the name of the output file (no need to spoecify output file type, 
    will always return
    text file.)
    postcondition: returns a txt output of the alignment and corresponding info
    '''
    os.system(f"blastn -task blastn -query {query} -subject {subject} -out {out}.txt")
