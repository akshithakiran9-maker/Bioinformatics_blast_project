# Bioinformatics_blast_project
Title: 

     In-silico Identification and Functional Characterization of a unknown Protein Using Sequence Analysis and Homology-Based Annotation.

Objective:

    To predict the biological function of an unknown protein (Accession:Q9Y3Z3) by analyzing sequence similarity, BLAST hits, and functional annotation.

Research Question

   When an unknown biological sequence is taken, how can computational tools be used 
to predict its similarity with other sequences and infer its potential biological function?
  
Tools used:

1.UniProt Database

        To retrieve the Hypothetical proetin and
 To retrieve functional annotation for top hits and high-identity homologs.
 
2.FASTA Sequence Files

       Input file: unknown_protein.fasta containing your unknown protein sequence (Q9Y3Z3).

3.Biopython (Python library)

      To parse BLAST XML results.

4.NCBI BLAST

     To perform sequence similarity search and find homologous proteins.

5.Python 3.11

      Used to run scripts for parsing BLAST results, filtering hits, and summarizing top hits.
Output downloaded in XML format for parsing.

6.VS Code 

    For writing Python scripts, organizing folders, and documenting results.


Pipeline / Workflow:

Single continuous Pipeline

1. Sequence Retrieval  
2. Sequence Quality Analysis
3. Sequence Filtering and Validation
4. Homology Search
5. Functional Annotation
6. Biological Interpretation
   

Methodology:

1.Sequence Retrieval
      The unknow protein sequence(Q9Y3Z3)from human Immunodeficiency virus (hiv),
 was retrived from UniPort databasein fasta formate.


2.Sequence Quality Analysis
     The sequence Qualityis checked for any invalid amino acids,and length using Biopython


3.Sequence filtering and Validation
     Sequence filtering is made to remove very short and low Quality aminoacid sequences.
It ensures no duplicates or invalid sequences were included.Unknown protein(Q9Y3Z3) is checked and validated .


4.Homology Search:
   - BLAST (Basic Local Alignment Search Tool) was used to find homologous sequences.
   - Parameters: default BLASTp settings, against protein database.
   - used xml format for the output, xml output was downloaded for further analysis.

5. Parsing BLAST Results:
   - Biopython scripts were used to parse xml output.
   - Extracted information included: accession number, protein title, e-value, identities, and % identity.

6. Filtering Top Hits:
   - Hits with high percentage identity (≥90%) and low e-values were selected.
   - The top hit (NP_001350662) was identified based on highest identity (100.0)and lowest e-value(0.0).So this hit
   was taken to predict and analyze the function of unknown Protein.

7. Functional Annotation:
   - UniProt database was used to retrieve functional information of the top hit(NP_001350662) .
   - High-identity homologs were also considered for additional functional insights.

8. Biological Interpretation:
   - Predicted the likely function of the unknown protein based on top hit and homologous sequences.
   - Documented top hit accession, identity, functional annotation, and notes in the top_hit folder.
  
   
Result:

This top hit was selected as the best match based on highest % identity and lowest E-value.

Top Hit Accession: NP_001350662

 Gene:SAMHD1
 
 Protein name: Deoxynucleoside triphosphate triphosphohydrolase SAMHD1
 
 E value :  0.0
 
 Identities : 582
 
 Identity% :100.0
 
This predicted function suggests that the unknown protein(Q9Y3Z3) likely plays a critical role in controlling viral replication and regulating intracellular dNTP levels, similar to the activity observed in SAMHD1 and related proteins.


