'''Uses SeqIO to handle all things for .ab1 files. Requires SeqIO from Bio'''
from Bio import SeqIO

#read ab1 file into Bio.SeqRecord.SeqRecord object
def read_ab1(f):
    '''
    precondition: accepts a string of the file name ab1 file
    postcondition: returns a Bio.SeqRecord.SeqRecord object made from the file
    '''
    record = SeqIO.read(f, "abi")
    return record


#extract base calls from Bio.SeqRecord.SeqRecord object
def base_calls(SeqRecord):
    '''
    precondition: accepts a SeqRecord from Bio.SeqIO
    postcondition: returns a string of the sequence from the
	Bio.Seq.Seq object made from the record.
    '''
    base_calls = SeqRecord.seq
    return base_calls