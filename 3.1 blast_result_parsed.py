
# ------------------------------------------------------------
# Project: Functional Annotation of Unknown Protein
# Step: Parsing BLAST XML results using BioPython
# Author: Akshitha Kiran
# Description: This script reads BLAST XML output and extracts
#              top hits, alignment length, E-value, and
#              percent identity.
# ------------------------------------------------------------
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

# Import required module for parsing BLAST XML output
from Bio.Blast import NCBIWWW
print("blast result is successful ")
protein_seq=NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence="MQRADSEQPSKRPRCDDSPRTPSNTPSAEADWSPGLELHPDYKTWGPEQVCSFLRRGGFEEPVLLKNIRENEITGALLPCLDESRFENLGVSSLGERKKLLSYIQRLVQIHVDTMKVINDPIHGHIELHPLLVRIIDTPQFQRLRYIKQLGGGYYVFPGASHNRFEHSLGVGYLAGCLVHALGEKQPELQISERDVLCVQIAGLCHDLGHGPFSHMFDGRFIPLARPEVKWTHEQGSVMMFEHLINSNGIKPVMEQYGLIPEEDICFIKEQIVGPLESPVEDSLWPYKGRPENKSFLYEIVSNKRNGIDVDKWDYFARDCHHLGIQNNFDYKRFIKFARVCEVDNELRICARDKEVGNLYDMFHTRNSLHRRAYQHKVGNIIDTMITDAFLKADDYIEITGAGGKKYRISTAIDDMEAYTKLTDNIFLEILYSTDPKLKDAREILKQIEYRNLFKYVGETQPTGQIKIKREDYESLPKEVASAKPKVLLDVKLKAEDFIVDVINMDYGMQEKNPIDHVSFYCKTAPNRAIRITKNQVSQLLPEKFAEQLIRVYCKKVDRKSLYAARQYFVQWCADRNFTKPQDGDVIAPLITPQKKEWNDTSVQNPTRLREASKSRVQLFKDDPM")
# Open previously generated BLAST XML result file
# and read the BLAST record

from Bio.Blast import NCBIXML
with open("blast_result.xml")as b:
        blast_record=NCBIXML.read(b)
        print(len(blast_record.alignments))
        print("total hit: ",len(blast_record.alignments)) # Print total number of BLAST hits obtained
        # Loop through top 10 alignments (best hits)
for alignment in blast_record.alignments[:10]:
        print("Title : ",alignment.title)
        print("length of hit : ",alignment.length)
        print("----"*100)
# Each alignment may contain multiple HSPs
# (High Scoring Segment Pairs)
        for alignment in blast_record.alignments[:50]:
                for hsp in alignment.hsps:
                     print("title : ",alignment.title)
                     print("E value : ",hsp.expect)
                     # Calculate percent identity of alignment
# Formula: (Identities / Alignment length) × 100
                     print("identities : ",hsp.identities)
                     percent_identity= (hsp.identities/
                 hsp.align_length)*100
                     print( percent_identity)
                     # Print separator for readability
                     print("   "*40)
# End of BLAST parsing analysis



        