# Protein Sequence Analysis Using Python

## Overview

This project performs a basic bioinformatics analysis of the Human Carbonic Anhydrase I (CA1) protein sequence using Python.

The project demonstrates how Python can be used to process a protein FASTA sequence, calculate amino acid composition, analyze basic physicochemical properties, and visualize the results.

## Protein Information

- **Protein:** Human Carbonic Anhydrase I (CA1)
- **Organism:** Homo sapiens
- **NCBI RefSeq:** NP_001729.1
- **Sequence length:** 261 amino acids

## Objectives

- Read and process a protein FASTA sequence
- Calculate amino acid composition
- Determine amino acid percentages
- Identify the most and least abundant amino acids
- Calculate basic protein properties
- Visualize amino acid composition
- Organize analysis results using Python and pandas

## Analysis Performed

### 1. Sequence Analysis

- FASTA header extraction
- Protein sequence extraction
- Protein length calculation
- Amino acid counting
- Amino acid percentage calculation

### 2. Amino Acid Composition

The project identifies the abundance of each amino acid and generates a bar chart showing the amino acid composition of the protein.

### 3. Biochemical Properties

The following properties were calculated:

- Molecular weight
- Isoelectric point (pI)
- Instability index
- Aliphatic index
- GRAVY (Grand Average of Hydropathy)

### 4. Amino Acid Groups

The sequence was also analyzed using simplified biochemical groups:

- Hydrophobic amino acids
- Polar amino acids
- Positively charged amino acids
- Negatively charged amino acids

## Tools and Libraries

- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- Biopython

## Project Structure

```text
Protein-Sequence-Analysis/
├── data/
│   └── CA1.FASTA.txt
├── Notebook/
│   └── Sequence_analysis.ipynb
├── Results/
│   ├── amino_acid_composition.png
│   ├── protein_analysis_summary.txt
│   └── protein_properties.csv
├── src/
│   └── sequence_analysis.py
├── README.md
├── requirements.txt
└── .gitignore