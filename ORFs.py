from Bio import SeqIO
from Bio.Seq import Seq

file_path="C:/Users/Heather P/Desktop/project夾/bioinfo/pj II/sequence.fas" 
seq_record = SeqIO.read(file_path, "fasta")
dna_sequence = str(seq_record.seq)

# Define the function to identify start and stop codons
def find_orfs(sequence, start_codon="ATG", stop_codons=["TAA", "TAG", "TGA"]):
    start_positions = []
    orfs = []
    i = 0
    while i < len(sequence):
        codon = sequence[i:i+3]
        if codon == start_codon:
            start_positions.append(i)
        elif codon in stop_codons and start_positions:
            orfs.append((start_positions[0], i+3))
            start_positions = []
        i += 3
    return orfs

# Identify the ORFs in the DNA sequence
orfs = find_orfs(dna_sequence)

protein_sequences = []
for orf in orfs:
    dna_seq = dna_sequence[orf[0]:orf[1]]
    # create a Seq object from the DNA sequence string
    seq = Seq(dna_seq)
    # translate the sequence and append the result to the protein_sequences list
    protein_seq = str(seq.translate())
    # check for stop codon in the translated sequence
    if '*' in protein_seq:
        # remove any amino acids that occur after the stop codon
        protein_seq = protein_seq[:protein_seq.index('*')]
    protein_sequences.append(protein_seq)

# Define the function to identify potential protein coding regions
def find_protein_coding_regions(sequences, start_sequence="M", stop_sequence="*"):
    start_positions = []
    coding_regions = []
    for i, seq in enumerate(sequences):
        if start_sequence in seq:
            start_positions.append(i)
        elif stop_sequence in seq and start_positions:
            coding_regions.append((start_positions[0], i+1))
            start_positions = []
    return coding_regions

# Identify potential protein coding regions
coding_regions = find_protein_coding_regions(protein_sequences)

# Print the identified ORFs and potential protein coding regions
print("ORFs:")
print(orfs)

if coding_regions:
    print("Potential protein coding regions:")
    print(coding_regions)
else:
    print("No potential protein coding regions found.")
