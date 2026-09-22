# Read the FASTA file

with open("D:/Protein-Sequence-Analysis/data/CA1.FASTA.txt", "r") as file:
    lines = file.readlines()
    

# Separate header and sequence

header = lines[0].strip()
sequence = "".join(line.strip() for line in lines[1:])

print("Header:")
print(header)

print("\nProtein sequence:")
print(sequence)

print("\nProtein length:", len(sequence))
