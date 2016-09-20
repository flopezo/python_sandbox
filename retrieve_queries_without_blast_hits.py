'''
Retrieve non-matching BLAST queries
http://biopython.org/wiki/Retrieve_nonmatching_blast_queries
Presume you set up a BLAST run with the sequences in a file called queries.fasta searched against a database, with the results saved to BLAST_RESULTS.xml
'''

from Bio import SeqIO
from Bio.Blast import NCBIXML

# Build an index, but we don't need to parse the record
q_dict = SeqIO.index("queries.fasta", "fasta")
output_handle = open("orphan_records.fasta", "w")

hits = []
for record in NCBIXML.parse(open("BLAST_RESULTS.xml")):
    # As of BLAST 2.2.19 the xml output for multiple-query blast searches
    # skips queries with no hits so we could just append the ID of every blast
    # record to our 'hit list'. It's possible that the NCBI will change this
    # behavior in the future so let's make the appending conditional on there
    # being some hits (i.e., a non-empty alignments list) recorded in the blast
    # record

    if record.alignments:
        # The blast record's 'query' contains the sequences description as a
        # string. We used the ID as the key in our dictionary so we'll need to
        # split the string and get the first field to remove the right entries
        hits.append(record.query.split()[0])

misses = set(q_dict.keys()) - set(hits)
orphan_records = [q_dict[name] for name in misses]

SeqIO.write(orphan_records, output_handle, "fasta")
output_handle.close()

print("found %i records in query, %i have hits, making %i misses"
      % (len(q_dict), len(hits), len(misses)))
