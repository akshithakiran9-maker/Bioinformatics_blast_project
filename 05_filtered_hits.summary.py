#filtering and validation
from Bio.Blast import NCBIXML
with open("blast_result.xml")as b:
        blast_record=NCBIXML.read(b)
#alignment for fisrt 5 top hits
for alignment in blast_record.alignments[:5]:
                for hsp in alignment.hsps:
                        print("title : ",alignment.title)
                        print("E value : ",hsp.expect)
                        print("identities : ",hsp.identities)
                        percent_identity= (hsp.identities/hsp.align_length)*100
                        print( percent_identity)
                        print("   "*40)

 #title: NP_001350662|deoxynucleoside triphosphate triphosphohydrolase SAMHD1 isoform 3 [Homo sapiens] >gb|KAI2594744.1| SAM and HD domain containing deoxynucleoside triphosphate triphosphohydrolase 1 [Homo sapiens] >gb|KAI4005454.1| SAM and HD domain containing deoxynucleoside triphosphate triphosphohydrolase 1 [Homo sapiens]
# E value :  0.0
# identities :  582
# identity% :100.0

#title :  ref|NP_056289.2| deoxynucleoside triphosphate triphosphohydrolase SAMHD1 isoform 1 [Homo sapiens] >sp|Q9Y3Z3.2
# E value :  0.0
# identities :  625
# 99.84025559105432

# title :  gb|AAF32407.1| hypothetical protein SBBI88 [Homo sapiens] >emb|CAB43368.1| hypothetical protein [Homo sapiens]
# E value :  0.0
# identities :  623
# 99.52076677316293
 
#  title :  gb|AAH36450.1| SAM domain and HD domain 1 [Homo sapiens] >gb|ADZ15537.1| SAM domain and HD domain 1, partial [synthetic construct] >gb|AIC56135.1| SAMHD1, partial [synthetic construct] >emb|SJX43904.1| unnamed protein product, partial [Human ORFeome Gateway entry vector]
# E value :  0.0
# identities :  623
# 99.52076677316293


# title :  ref|NP_001266115.1| deoxynucleoside triphosphate triphosphohydrolase SAMHD1 [Pan paniscus] >ref|NP_001267439.1| deoxynucleoside triphosphate triphosphohydrolase SAMHD1 [Pan troglodytes] >gb|AFB71157.1| SAM domain and HD domain-containing protein 1 [Pan troglodytes] >gb|AFB71158.1| SAM domain and HD domain-containing protein 1 [Pan paniscus] >gb|AFJ79636.1| SAM domain and HD domain-containing protein 1 [Pan troglodytes] >gb|AFJ79637.1| 
# SAM domain and HD domain-containing protein 1 [Pan troglodytes] 
# >gb|AFU88758.1| SAM domain and HD domain-containing protein [Pan troglodytes]
# E value :  0.0
# identities :  621
# 99.2012779552715


