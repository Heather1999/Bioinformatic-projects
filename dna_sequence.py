gc_count = 0
with open("C:\\Users\\Heather P\\Desktop\\project夾\\bioinfo\\dna_sequence.txt", "r") as f:
    sequence = f.read().strip().upper().replace("\n", "")
    print(f"Sequence length: {len(sequence)}")
for base in sequence:
    if base in ["G", "C"]:
        gc_count += 1
gc_content = gc_count / len(sequence) * 100
print(f"GC content: {gc_content:.2f}%")
complement_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
reverse_complement = ""
for base in reversed(sequence):
    if base not in complement_dict:
        print(f"Invalid base '{base}' found in sequence")
        continue
    reverse_complement += complement_dict[base]
print(f"Reverse complement: {reverse_complement}")
