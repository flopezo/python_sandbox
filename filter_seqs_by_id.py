from Bio import SeqIO

'''
Filtering a sequence file
"Often you’ll have a large file with many sequences in it (e.g. FASTA file or genes, or a FASTQ or SFF file of reads), a separate shorter list of the IDs for a subset of sequences of interest, and want to make a new sequence file for this subset."
http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc280
Search for TaxonID in FASTA file
'''

input_file = "infile.fasta"
output_file = "outfile.fasta"

records = (r for r in SeqIO.parse(input_file, "fasta") if "TaxonID" in r.id)
# Use "TAXONID" in r.id.upper() when working with IDs such as TaxonID, taxonid, Taxonid and so on 
# records = (r for r in SeqIO.parse(input_file, "fasta") if "TAXONID" in r.id.upper())
count = SeqIO.write(records, output_file, "fasta")
print("Saved %i records from %s to %s" % (count, input_file, output_file))